"""
Extract color CSS custom properties from _root.scss and write them to
_data/color-vars.yml for use in Jekyll documentation tables.

Grouped by semantic category (text, link, border, background, status,
department-scale, department-background, department-text, department-border,
department-icon).

The `usage` field is preserved from an existing color-vars.yml when present.
New entries receive a generated default description.

Run: python3 extract_root_colors.py

No external dependencies required.
"""

import os
import re

ROOT_SCSS = os.path.join('src', 'scss', 'base', '_root.scss')
OUTPUT_YAML = os.path.join('_data', 'color-vars.yml')

CATEGORIES = (
    'text',
    'link',
    'border',
    'background',
    'status',
    'department-scale',
    'department-background',
    'department-text',
    'department-border',
    'department-icon',
)

# Maps comment markers in _root.scss to category keys
SECTION_MARKERS = {
    '// Text colors': 'text',
    '// Border colors': 'border',
    '// Background colors': 'background',
    '// Status colors': 'status',
    '// Department color scales': 'department-scale',
    '// Icons colors': '_end',
}

# Prefixes allowed per category (guards against stray matches)
CATEGORY_PREFIXES = {
    'text': ('color-text-',),
    'link': ('color-link',),
    'border': ('color-border-',),
    'background': ('color-background-',),
    'status': ('color-status-',),
    'department-scale': ('color-',),
}

DEPARTMENT_SLUGS = (
    'scienzeumane',
    'agroalimentari',
    'biomedica',
    'ingegneria',
    'ambiente',
    'chimica',
    'fisica',
)

DEPARTMENT_LABELS = {
    'fisica': 'Scienze fisiche e tecnologie della materia',
    'ambiente': 'Scienze del sistema terra e tecnologie per l\'ambiente',
    'biomedica': 'Scienze biomediche',
    'ingegneria': 'Ingegneria',
    'scienzeumane': 'Scienze umane',
    'chimica': 'Scienze chimiche',
    'agroalimentari': 'Scienze bio-agroalimentari',
}

DEPARTMENT_SEMANTIC_PREFIXES = (
    ('color-background-', 'department-background'),
    ('color-text-', 'department-text'),
    ('color-border-', 'department-border'),
    ('icon-', 'department-icon'),
)

SCALE_WEIGHT_USAGE = {
    '200': 'tonalità chiara (sfondi soft, badge)',
    '500': 'colore principale del dipartimento',
    '600': 'hover, stati attivi e testo su sfondi chiari',
    '800': 'testo, icone e stati pressed',
}

SYSTEM_STATUS_LABELS = {
    'danger': 'pericolo',
    'warning': 'allerta',
    'success': 'successo',
    'info': 'informazione',
}

SEMANTIC_SUFFIX_USAGE = {
    '': 'sfondo principale',
    '-light': 'sfondo chiaro',
    '-hover': 'sfondo per lo stato hover',
    '-active': 'sfondo per lo stato active/premuto',
}

TEXT_SUFFIX_USAGE = {
    '': 'testo su sfondo chiaro',
    '-hover': 'testo per lo stato hover',
    '-active': 'testo per lo stato active/premuto',
}

BORDER_SUFFIX_USAGE = TEXT_SUFFIX_USAGE
ICON_SUFFIX_USAGE = TEXT_SUFFIX_USAGE

# Variables to exclude even if they match the pattern
EXCLUDED_VARS = {
    'color-code',
    'color-outline-focus',
}

VAR_RE = re.compile(r'\s--#\{\$prefix\}([a-z][a-z0-9-]*):\s')
SCALE_RE = re.compile(r'^color-([a-z]+)-(200|500|600|800)$')


def infer_swatch(var_name):
    """Return the default swatch type for a CSS variable name."""
    if var_name in ('color-border-inverse',):
        return 'border-inverse'
    if var_name.startswith('color-border-'):
        return 'border'
    if var_name in ('color-text-inverse', 'color-link-inverse'):
        return 'inverse-nested'
    if var_name == 'color-background-inverse':
        return 'bg-border'
    return 'bg'


def department_slug_from_suffix(suffix):
    """Extract department slug from the part after a semantic prefix."""
    for slug in DEPARTMENT_SLUGS:
        if suffix == slug or suffix.startswith(slug + '-'):
            return slug
    return None


def infer_department_semantic_category(var_suffix):
    """Route department semantic variables to documentation categories."""
    for prefix, category in DEPARTMENT_SEMANTIC_PREFIXES:
        if not var_suffix.startswith(prefix):
            continue
        rest = var_suffix[len(prefix):]
        if department_slug_from_suffix(rest):
            return category
    return None


def is_department_scale(var_suffix):
    match = SCALE_RE.match(var_suffix)
    if not match:
        return False
    return match.group(1) in DEPARTMENT_SLUGS


def strip_yaml_scalar(value):
    """Normalize a scalar read from a minimal YAML line."""
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in ('"', "'"):
        return bytes(value[1:-1], 'utf-8').decode('unicode_escape')
    return value


def system_semantic_usage(var_suffix, category):
    """Generate usage text for system status color variables."""
    status = next((name for name in SYSTEM_STATUS_LABELS if f'-{name}' in var_suffix), None)
    if status is None:
        return ''

    label = SYSTEM_STATUS_LABELS[status]

    if category == 'text':
        if var_suffix.endswith('-active'):
            return f'Testo di {label} per lo stato active'
        if var_suffix.endswith('-hover'):
            return f'Testo di {label} per lo stato hover'
        return f'Testo per stati di {label}'

    if category == 'border':
        if var_suffix.endswith('-active'):
            return f'Bordo di {label} per lo stato active'
        if var_suffix.endswith('-hover'):
            return f'Bordo di {label} per lo stato hover'
        return f'Bordo di {label}'

    if category == 'background':
        if var_suffix.endswith('-active'):
            return f'Sfondo di {label} per lo stato active'
        if var_suffix.endswith('-hover'):
            return f'Sfondo di {label} per lo stato hover'
        if var_suffix.endswith('-light'):
            return f'Sfondo di {label} chiaro (contenuti medio-lunghi)'
        return f'Sfondo per stati di {label}'

    if category == 'status':
        if var_suffix.endswith('-active'):
            return f'Indicatore {label} per lo stato active'
        if var_suffix.endswith('-hover'):
            return f'Indicatore {label} per lo stato hover'
        return f'Colore indicatore di {label}'

    return ''


def default_usage(full_var, category):
    """Generate Italian usage text for new variables."""
    var_suffix = full_var.replace('--bsi-', '')

    system_usage = system_semantic_usage(var_suffix, category)
    if system_usage:
        return system_usage

    if category == 'department-scale':
        match = SCALE_RE.match(var_suffix)
        if not match:
            return ''
        slug, weight = match.group(1), match.group(2)
        label = DEPARTMENT_LABELS.get(slug, slug)
        weight_text = SCALE_WEIGHT_USAGE.get(weight, f'tonalità {weight}')
        return f'{label}: {weight_text}'

    slug = None
    semantic_suffix = ''
    for prefix, cat in DEPARTMENT_SEMANTIC_PREFIXES:
        if category != cat or not var_suffix.startswith(prefix):
            continue
        rest = var_suffix[len(prefix):]
        slug = department_slug_from_suffix(rest)
        if slug:
            semantic_suffix = rest[len(slug):]
            break

    if not slug:
        return ''

    label = DEPARTMENT_LABELS.get(slug, slug)

    if category == 'department-background':
        detail = SEMANTIC_SUFFIX_USAGE.get(semantic_suffix, 'sfondo')
    elif category == 'department-text':
        detail = TEXT_SUFFIX_USAGE.get(semantic_suffix, 'testo')
    elif category == 'department-border':
        detail = BORDER_SUFFIX_USAGE.get(semantic_suffix, 'bordo')
    elif category == 'department-icon':
        detail = ICON_SUFFIX_USAGE.get(semantic_suffix, 'icona')
    else:
        detail = ''

    return f'{label}: {detail}'


def parse_root_scss():
    """Parse _root.scss and return a dict {category: [{'var': ..., 'swatch': ...}]}."""
    result = {cat: [] for cat in CATEGORIES}
    current_category = None
    department_semantic_mode = False

    with open(ROOT_SCSS, encoding='utf-8') as f:
        for line in f:
            stripped = line.strip()

            if stripped.startswith('// Department semantic tokens'):
                department_semantic_mode = True
                current_category = None
                continue

            for marker, cat in SECTION_MARKERS.items():
                if stripped == marker or stripped.startswith(marker + ' '):
                    if cat == '_end':
                        department_semantic_mode = False
                        current_category = None
                    else:
                        current_category = cat
                        department_semantic_mode = False
                    break

            if stripped.startswith('//') and not stripped.startswith('// Department semantic tokens'):
                if not stripped.startswith('// Department semantic tokens'):
                    pass

            if stripped.startswith('//'):
                continue

            m = VAR_RE.search(line)
            if not m:
                continue

            var_suffix = m.group(1)

            if var_suffix in EXCLUDED_VARS:
                continue

            if department_semantic_mode:
                target_cat = infer_department_semantic_category(var_suffix)
                if target_cat is None:
                    continue
            elif current_category == 'department-scale':
                if not is_department_scale(var_suffix):
                    continue
                target_cat = current_category
            elif current_category is None:
                continue
            elif current_category == 'text' and var_suffix.startswith('color-link'):
                target_cat = 'link'
            else:
                target_cat = current_category
                allowed = CATEGORY_PREFIXES.get(target_cat, ())
                if not any(var_suffix.startswith(p) for p in allowed):
                    continue

            full_var = f'--bsi-{var_suffix}'
            result[target_cat].append({
                'var': full_var,
                'swatch': infer_swatch(var_suffix),
            })

    return result


def load_existing_yaml():
    """Load current color-vars.yml if it exists; return empty dict otherwise."""
    if not os.path.exists(OUTPUT_YAML):
        return {}

    data = {cat: [] for cat in CATEGORIES}
    current_cat = None
    current_entry = None

    with open(OUTPUT_YAML, encoding='utf-8') as f:
        for line in f:
            if re.match(r'^[a-z-]+:\s*$', line):
                current_cat = line.strip().rstrip(':')
                current_entry = None
                continue

            if line.startswith('- var:'):
                current_entry = {'var': line.split(':', 1)[1].strip()}
                if current_cat in data:
                    data[current_cat].append(current_entry)
                continue

            if current_entry is None:
                continue

            if line.startswith('  swatch:'):
                current_entry['swatch'] = line.split(':', 1)[1].strip()
            elif line.startswith('  usage:'):
                current_entry['usage'] = strip_yaml_scalar(line.split(':', 1)[1])

    return {k: v for k, v in data.items() if v}


def build_usage_index(existing):
    """Build a flat {var_name: entry} index from existing YAML for fast lookup."""
    index = {}
    for entries in existing.values():
        if not isinstance(entries, list):
            continue
        for entry in entries:
            if 'var' in entry:
                index[entry['var']] = entry
    return index


def merge(parsed, existing_index):
    """
    Merge newly parsed vars with existing data:
    - Preserve 'usage' and manual 'swatch' from existing entries.
    - Add default usage for new entries.
    - Warn about removed entries.
    """
    merged = {}
    all_new_vars = {e['var'] for entries in parsed.values() for e in entries}

    for old_var in existing_index:
        if old_var not in all_new_vars:
            print(f'[WARNING] Variable removed from _root.scss: {old_var}')

    for cat, entries in parsed.items():
        merged[cat] = []
        for entry in entries:
            var = entry['var']
            if var in existing_index:
                old = existing_index[var]
                merged_entry = {'var': var, 'swatch': old.get('swatch', entry['swatch'])}
                usage = old.get('usage')
            else:
                merged_entry = {'var': var, 'swatch': entry['swatch']}
                usage = default_usage(var, cat)

            if usage:
                merged_entry['usage'] = usage
            merged[cat].append(merged_entry)

    return merged


def write_yaml(data):
    lines = []
    for cat in CATEGORIES:
        entries = data.get(cat, [])
        if not entries:
            continue
        lines.append(f'{cat}:')
        for entry in entries:
            lines.append(f'- var: {entry["var"]}')
            lines.append(f'  swatch: {entry["swatch"]}')
            if entry.get('usage'):
                usage = entry['usage'].replace('\\', '\\\\').replace('"', '\\"')
                lines.append(f'  usage: "{usage}"')
        lines.append('')

    with open(OUTPUT_YAML, 'w', encoding='utf-8') as f:
        f.write('\n'.join(lines).rstrip() + '\n')


if __name__ == '__main__':
    parsed = parse_root_scss()
    existing = load_existing_yaml()
    existing_index = build_usage_index(existing)
    merged = merge(parsed, existing_index)
    write_yaml(merged)
    total = sum(len(v) for v in merged.values())
    print(f'Written {total} color variables to {OUTPUT_YAML}')
    for cat, entries in merged.items():
        missing = [e['var'] for e in entries if 'usage' not in e]
        if missing:
            print(f'  [{cat}] {len(missing)} entries without usage: {", ".join(missing)}')
