---
layout: docs
title: Ombreggiature
description: Aggiungi o rimuovi ombreggiature con questa utility.
group: organizzare-gli-spazi
toc: true
---

Le ombreggiature del tema CNR usano il blu primario (`#002f5f`) al 15% di opacità, con tre livelli di blur definiti dal UI Kit.

## Varianti di profondità

{% comment %}Example name: Varianti di profondità{% endcomment %}
{% capture example %}
<div class="shadow-none p-3 mb-5 bg-light">Nessuna ombra</div>
<div class="shadow-sm p-3 mb-5 bg-white">Ombra piccola (shadow-s)</div>
<div class="shadow-md p-3 mb-5 bg-white">Ombra media (shadow-m)</div>
<div class="shadow-lg p-3 mb-5 bg-white">Ombra grande (shadow-l)</div>
{% endcapture %}
{% include example.html content=example %}

Sono disponibili anche le classi alias `.shadow-s`, `.shadow-m` e `.shadow-l`, equivalenti rispettivamente a `.shadow-sm`, `.shadow-md` e `.shadow-lg`.

## Variabili CSS

| Classe utility | Variabile CSS | Valore |
| -------------- | ------------- | ------ |
| `.shadow-sm` / `.shadow-s` | `--bsi-shadow-s` | `0 0 4px 0 rgba(0, 47, 95, 0.15)` |
| `.shadow-md` / `.shadow-m` | `--bsi-shadow-m` | `0 0 16px 0 rgba(0, 47, 95, 0.15)` |
| `.shadow-lg` / `.shadow-l` | `--bsi-shadow-l` | `0 0 48px 0 rgba(0, 47, 95, 0.15)` |
{: .table .table-cols-equal .mb-4}

Ogni ombra espone anche i token primitivi (`--bsi-shadow-s-x`, `--bsi-shadow-s-blur`, `--bsi-shadow-s-color`, ecc.) per personalizzazioni granulari. Le variabili legacy `--bsi-elevation-low`, `--bsi-elevation-medium` e `--bsi-elevation-high` restano disponibili come alias.

Per l'elenco completo consulta la pagina [Variabili CSS]({{ site.baseurl }}/docs/personalizzare-la-libreria/variabili-css/).
