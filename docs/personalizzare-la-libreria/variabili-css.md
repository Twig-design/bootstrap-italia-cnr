---
layout: docs
group: personalizzare-la-libreria
toc: true

title: Variabili CSS
description: Utilizza le variabili CSS di Bootstrap Italia per personalizzare la libreria a runtime.
---

## Introduzione

Dalla versione 3, Bootstrap Italia usa le CSS custom properties (o variabili CSS) per definire gli stili degli elementi e componenti della libreria. Questo consente di personalizzare ogni aspetto dell'interfaccia a runtime **senza la necessità di ricompilare i file SCSS**. Ad esempio, per cambiare il colore del testo primario, basta sovrascrivere la variabile `--bsi-color-text-primary` nel tuo CSS o SCSS dedicato. 

Questo approccio **sostituisce il sistema precedente basato su variabili Sass**, semplificando la personalizzazione.

Tutte le variabili CSS di Bootstrap Italia usano il prefisso `bsi-`.

## Variabili globali
 
Le variabili globali sono definite nel file `_root.scss` e possono essere usate in qualsiasi punto del codice CSS della libreria, seguendo il principio del *cascading*. Il file `_root.scss` è incluso in `bootstrap-italia.scss` e viene importato tramite la direttiva `@forward`:

```scss
// bootstrap-italia.scss
@forward 'base/root';
```

### Lista completa

I token colore personalizzati per il CNR sono documentati con tabelle interattive nella pagina [Colori]({{ site.baseurl }}/docs/personalizzare-la-libreria/colori/). Di seguito un estratto fedele delle variabili globali definite in `_root.scss`.

```scss
  // Theme colors
  --#{$prefix}theme-primary: #{$theme-primary};
  --#{$prefix}theme-primary-light: #{$theme-primary-light};
  --#{$prefix}theme-primary-lighter: #{$theme-primary-lighter};
  --#{$prefix}theme-primary-subtle: #{$theme-primary-subtle};
  --#{$prefix}theme-primary-muted: #{$theme-primary-muted};
  --#{$prefix}theme-primary-deep: #{$theme-primary-deep};

  // Typography
  --#{$prefix}font-mono: #{tokens.$it-font-mono};
  --#{$prefix}font-serif: #{tokens.$it-font-serif};
  --#{$prefix}font-sans: 'Titillium Web', 'Titillium Sans Pro', #{tokens.$it-font-sans};
  --#{$prefix}font-weight-strong: #{tokens.$it-font-weight-bold};
  --#{$prefix}font-weight-solid: #{tokens.$it-font-weight-semibold};
  --#{$prefix}font-weight-base: #{tokens.$it-font-weight-regular};
  --#{$prefix}font-weight-thin: #{tokens.$it-font-weight-light};
  --#{$prefix}font-size-11: #{tokens.$it-font-size-11};
  --#{$prefix}font-size-10: #{tokens.$it-font-size-10};
  --#{$prefix}font-size-9: #{tokens.$it-font-size-9};
  --#{$prefix}font-size-8: #{tokens.$it-font-size-8};
  --#{$prefix}font-size-7: #{tokens.$it-font-size-7};
  --#{$prefix}font-size-6: #{tokens.$it-font-size-6};
  --#{$prefix}font-size-5: #{tokens.$it-font-size-5};
  --#{$prefix}font-size-4: #{tokens.$it-font-size-4};
  --#{$prefix}font-size-3: #{tokens.$it-font-size-3};
  --#{$prefix}font-size-2: #{tokens.$it-font-size-2};
  --#{$prefix}font-size-1: #{tokens.$it-font-size-1};
  --#{$prefix}font-leading-5: #{tokens.$it-font-leading-5};
  --#{$prefix}font-leading-4: #{tokens.$it-font-leading-4};
  --#{$prefix}font-leading-3: #{tokens.$it-font-leading-3};
  --#{$prefix}font-leading-2: #{tokens.$it-font-leading-2};
  --#{$prefix}font-leading-1: #{tokens.$it-font-leading-1};
  --#{$prefix}font-tracking-normal: #{tokens.$it-font-tracking-normal};
  --#{$prefix}font-tracking-tight: #{tokens.$it-font-tracking-tight};
  --#{$prefix}font-tracking-narrow: #{tokens.$it-font-tracking-narrow};
  --#{$prefix}font-tracking-short: #{tokens.$it-font-tracking-short};
  --#{$prefix}display-font-size: #{tokens.$it-font-size-11};
  --#{$prefix}heading-6-font-size: #{tokens.$it-heading-6-font-size};
  --#{$prefix}heading-5-font-size: #{tokens.$it-heading-5-font-size};
  --#{$prefix}heading-4-font-size: #{tokens.$it-heading-4-font-size};
  --#{$prefix}heading-3-font-size: #{tokens.$it-heading-3-font-size};
  --#{$prefix}heading-2-font-size: #{tokens.$it-heading-2-font-size};
  --#{$prefix}heading-1-font-size: #{tokens.$it-heading-1-font-size};
  --#{$prefix}heading-font-weight: #{tokens.$it-heading-font-weight};
  --#{$prefix}heading-font-weight-weak: #{tokens.$it-heading-font-weight-weak};
  --#{$prefix}heading-leading: #{tokens.$it-heading-leading};
  --#{$prefix}body-font-size: #{tokens.$it-body-font-size};
  --#{$prefix}body-leading: #{tokens.$it-body-leading};
  --#{$prefix}body-font-weight: #{tokens.$it-body-font-weight};
  --#{$prefix}lead-font-size: #{tokens.$it-lead-font-size};
  --#{$prefix}lead-leading: #{tokens.$it-lead-leading};
  --#{$prefix}lead-font-weight: #{tokens.$it-lead-font-weight};
  --#{$prefix}caption-font-size: #{tokens.$it-caption-font-size};
  --#{$prefix}caption-leading: #{tokens.$it-caption-leading};
  --#{$prefix}caption-font-weight-regular: #{tokens.$it-caption-font-weight-regular};
  --#{$prefix}caption-font-weight-semibold: #{tokens.$it-caption-font-weight-semibold};
  --#{$prefix}label-font-size: #{tokens.$it-label-font-size};
  --#{$prefix}label-font-size-s: #{tokens.$it-label-font-size-s};
  --#{$prefix}label-font-size-xs: #{tokens.$it-label-font-size-xs};
  --#{$prefix}label-font-size-l: #{tokens.$it-label-font-size-l};
  --#{$prefix}label-leading: #{tokens.$it-label-leading};
  
  // Typography responsive properties
  @include media-breakpoint-up(sm) {
    --#{$prefix}heading-1-font-size: #{tokens.$it-heading-1-font-size-l};
    --#{$prefix}heading-2-font-size: #{tokens.$it-heading-2-font-size-l};
    --#{$prefix}heading-3-font-size: #{tokens.$it-heading-3-font-size-l};
    --#{$prefix}heading-4-font-size: #{tokens.$it-heading-4-font-size-l};
    --#{$prefix}heading-5-font-size: #{tokens.$it-heading-5-font-size-l};
    --#{$prefix}heading-6-font-size: #{tokens.$it-heading-6-font-size-l};
    --#{$prefix}lead-font-size: #{tokens.$it-lead-font-size-l};
    --#{$prefix}body-font-size: #{tokens.$it-body-font-size-l};
  }

  // Icons
  --#{$prefix}icon-size-xl: #{tokens.$it-icon-size-xl};
  --#{$prefix}icon-size-l: #{tokens.$it-icon-size-l};
  --#{$prefix}icon-size-m: #{tokens.$it-icon-size-m};
  --#{$prefix}icon-size-s: #{tokens.$it-icon-size-s};
  --#{$prefix}icon-size-xs: #{tokens.$it-icon-size-xs};

  // Border
  --#{$prefix}border-width: 1px;
  --#{$prefix}border-style: solid;
  --#{$prefix}border-color: #{$color-border-subtle};
  --#{$prefix}border-broad: #{$border-broad};
  --#{$prefix}border-thick: #{$border-thick};
  --#{$prefix}border-double: #{$border-double};
  --#{$prefix}border-base: #{$border-base};
  --#{$prefix}radius-rounded: #{$radius-rounded};
  --#{$prefix}radius-circle: #{$radius-circle};
  --#{$prefix}radius-smooth: #{$radius-smooth};
  --#{$prefix}radius-brand-sm: #{$radius-brand-sm};
  --#{$prefix}radius-brand-md: #{$radius-brand-md};
  --#{$prefix}radius-brand-lg: #{$radius-brand-lg};

  // Sizing
  --#{$prefix}sizing-full: #{tokens.$it-sizing-full};
  --#{$prefix}sizing-two-thirds: #{tokens.$it-sizing-two-thirds};
  --#{$prefix}sizing-half: #{tokens.$it-sizing-half};
  --#{$prefix}sizing-quarter: #{tokens.$it-sizing-quarter};

  // Shadow
  --#{$prefix}shadow-s-x: #{$shadow-s-x};
  --#{$prefix}shadow-s-y: #{$shadow-s-y};
  --#{$prefix}shadow-s-blur: #{$shadow-s-blur};
  --#{$prefix}shadow-s-spread: #{$shadow-s-spread};
  --#{$prefix}shadow-s-color: #{$shadow-s-color};
  --#{$prefix}shadow-s: #{$shadow-s};
  --#{$prefix}shadow-m-x: #{$shadow-m-x};
  --#{$prefix}shadow-m-y: #{$shadow-m-y};
  --#{$prefix}shadow-m-blur: #{$shadow-m-blur};
  --#{$prefix}shadow-m-spread: #{$shadow-m-spread};
  --#{$prefix}shadow-m-color: #{$shadow-m-color};
  --#{$prefix}shadow-m: #{$shadow-m};
  --#{$prefix}shadow-l-x: #{$shadow-l-x};
  --#{$prefix}shadow-l-y: #{$shadow-l-y};
  --#{$prefix}shadow-l-blur: #{$shadow-l-blur};
  --#{$prefix}shadow-l-spread: #{$shadow-l-spread};
  --#{$prefix}shadow-l-color: #{$shadow-l-color};
  --#{$prefix}shadow-l: #{$shadow-l};
  --#{$prefix}elevation-low: #{$shadow-s};
  --#{$prefix}elevation-medium: #{$shadow-m};
  --#{$prefix}elevation-high: #{$shadow-l};

  // Spacing
  --#{$prefix}spacing-3xl: #{tokens.$it-spacing-3xl};
  --#{$prefix}spacing-xxl: #{tokens.$it-spacing-xxl};
  --#{$prefix}spacing-xl: #{tokens.$it-spacing-xl};
  --#{$prefix}spacing-l: #{tokens.$it-spacing-l};
  --#{$prefix}spacing-m: #{tokens.$it-spacing-m};
  --#{$prefix}spacing-s: #{tokens.$it-spacing-s};
  --#{$prefix}spacing-14x: #{tokens.$it-spacing-14x};
  --#{$prefix}spacing-xs: #{tokens.$it-spacing-xs};
  --#{$prefix}spacing-xxs: #{tokens.$it-spacing-xxs};
  --#{$prefix}spacing-3xs: #{tokens.$it-spacing-3xs};
  --#{$prefix}heading-spacing: #{tokens.$it-spacing-s};
  --#{$prefix}paragraph-spacing: #{tokens.$it-spacing-m};

  // Text colors
  --#{$prefix}color-text-accent: #{$color-text-accent};
  --#{$prefix}color-text-inverse: #{tokens.$it-color-text-inverse};
  --#{$prefix}color-text-danger-active: #{$color-text-danger-active};
  --#{$prefix}color-text-danger-hover: #{$color-text-danger-hover};
  --#{$prefix}color-text-danger: #{$color-text-danger};
  --#{$prefix}color-text-warning-active: #{$color-text-warning-active};
  --#{$prefix}color-text-warning-hover: #{$color-text-warning-hover};
  --#{$prefix}color-text-warning: #{$color-text-warning};
  --#{$prefix}color-text-success-active: #{$color-text-success-active};
  --#{$prefix}color-text-success-hover: #{$color-text-success-hover};
  --#{$prefix}color-text-success: #{$color-text-success};
  --#{$prefix}color-text-info-active: #{$color-text-info-active};
  --#{$prefix}color-text-info-hover: #{$color-text-info-hover};
  --#{$prefix}color-text-info: #{$color-text-info};
  --#{$prefix}color-text-disabled: #{tokens.$it-color-text-disabled};
  --#{$prefix}color-text-muted: #{$color-text-muted};
  --#{$prefix}color-text-secondary: #{$color-text-secondary};
  --#{$prefix}color-text-primary: #{$color-text-primary};
  --#{$prefix}color-text-base: #{tokens.$it-color-text-base};
  --#{$prefix}color-code: #{tokens.$it-color-red-44};
  --#{$prefix}color-link: #{$color-link};
  --#{$prefix}color-link-hover: #{$color-link-hover};
  --#{$prefix}color-link-active: #{$color-link-active};
  --#{$prefix}color-link-secondary: #{$color-link-secondary};
  --#{$prefix}color-link-secondary-hover: #{$color-link-secondary-hover};
  --#{$prefix}color-link-secondary-active: #{$color-link-secondary-active};
  --#{$prefix}color-link-inverse: #{tokens.$it-color-link-inverse};
  --#{$prefix}color-link-disabled: #{tokens.$it-color-link-disabled};
  --#{$prefix}color-link-accent: #{$color-link-accent};
  --#{$prefix}color-link-accent-hover: #{$color-link-accent-hover};

  // Border colors
  --#{$prefix}color-border-danger-active: #{$color-border-danger-active};
  --#{$prefix}color-border-danger-hover: #{$color-border-danger-hover};
  --#{$prefix}color-border-danger: #{$color-border-danger};
  --#{$prefix}color-border-warning-active: #{$color-border-warning-active};
  --#{$prefix}color-border-warning-hover: #{$color-border-warning-hover};
  --#{$prefix}color-border-warning: #{$color-border-warning};
  --#{$prefix}color-border-success-active: #{$color-border-success-active};
  --#{$prefix}color-border-success-hover: #{$color-border-success-hover};
  --#{$prefix}color-border-success: #{$color-border-success};
  --#{$prefix}color-border-info-active: #{$color-border-info-active};
  --#{$prefix}color-border-info-hover: #{$color-border-info-hover};
  --#{$prefix}color-border-info: #{$color-border-info};
  --#{$prefix}color-border-subtle: #{$color-border-subtle};
  --#{$prefix}color-border-disabled: #{tokens.$it-color-border-disabled};
  --#{$prefix}color-border-inverse: #{tokens.$it-color-border-inverse};
  --#{$prefix}color-border-secondary-active: #{$color-border-secondary-active};
  --#{$prefix}color-border-secondary-hover: #{$color-border-secondary-hover};
  --#{$prefix}color-border-secondary: #{$color-border-secondary};
  --#{$prefix}color-border-primary-active: #{$color-border-primary-active};
  --#{$prefix}color-border-primary-hover: #{$color-border-primary-hover};
  --#{$prefix}color-border-primary: #{$color-border-primary};
  --#{$prefix}color-outline-focus: #{tokens.$it-color-outline-focus};

  // Background colors
  --#{$prefix}color-background-primary: #{$color-background-primary};
  --#{$prefix}color-background-primary-lighter: #{$color-background-primary-lighter};
  --#{$prefix}color-background-primary-light: #{$color-background-primary-light};
  --#{$prefix}color-background-primary-deep: #{$color-background-primary-deep};
  --#{$prefix}color-background-primary-muted: #{$color-background-primary-muted};
  --#{$prefix}color-background-primary-active: #{$color-background-primary-active};
  --#{$prefix}color-background-primary-hover: #{$color-background-primary-hover};
  --#{$prefix}color-background-danger-active: #{$color-background-danger-active};
  --#{$prefix}color-background-danger-hover: #{$color-background-danger-hover};
  --#{$prefix}color-background-danger-light: #{$color-background-danger-light};
  --#{$prefix}color-background-danger: #{$color-background-danger};
  --#{$prefix}color-background-warning-active: #{$color-background-warning-active};
  --#{$prefix}color-background-warning-hover: #{$color-background-warning-hover};
  --#{$prefix}color-background-warning-light: #{$color-background-warning-light};
  --#{$prefix}color-background-warning: #{$color-background-warning};
  --#{$prefix}color-background-success-active: #{$color-background-success-active};
  --#{$prefix}color-background-success-hover: #{$color-background-success-hover};
  --#{$prefix}color-background-success-light: #{$color-background-success-light};
  --#{$prefix}color-background-success: #{$color-background-success};
  --#{$prefix}color-background-info-active: #{$color-background-info-active};
  --#{$prefix}color-background-info-hover: #{$color-background-info-hover};
  --#{$prefix}color-background-info-light: #{$color-background-info-light};
  --#{$prefix}color-background-info: #{$color-background-info};
  --#{$prefix}color-background-emphasis: #{$color-background-emphasis};
  --#{$prefix}color-background-subtle: #{$color-background-subtle};
  --#{$prefix}color-background-disabled: #{tokens.$it-color-background-disabled};
  --#{$prefix}color-background-inverse: #{tokens.$it-color-background-inverse};
  --#{$prefix}color-background-inverse-hover: #{tokens.$it-color-slate-93};
  --#{$prefix}color-background-muted: #{$color-background-muted};
  --#{$prefix}color-background-accent-hover: #{$color-background-accent-hover};
  --#{$prefix}color-background-accent: #{$color-background-accent};
  --#{$prefix}color-background-secondary-lighter: #{$color-background-secondary-lighter};
  --#{$prefix}color-background-secondary-light: #{$color-background-secondary-light};
  --#{$prefix}color-background-secondary-active: #{$color-background-secondary-active};
  --#{$prefix}color-background-secondary-hover: #{$color-background-secondary-hover};
  --#{$prefix}color-background-secondary: #{$color-background-secondary};
  --#{$prefix}color-background-secondary-deep: #{$color-background-secondary-deep};

  // Status colors
  --#{$prefix}color-status-danger: #{$color-background-danger};
  --#{$prefix}color-status-danger-hover: #{$color-background-danger-hover};
  --#{$prefix}color-status-danger-active: #{$color-background-danger-active};
  --#{$prefix}color-status-success: #{$color-background-success};
  --#{$prefix}color-status-success-hover: #{$color-background-success-hover};
  --#{$prefix}color-status-success-active: #{$color-background-success-active};
  --#{$prefix}color-status-warning: #{$color-background-warning};
  --#{$prefix}color-status-warning-hover: #{$color-background-warning-hover};
  --#{$prefix}color-status-warning-active: #{$color-background-warning-active};
  --#{$prefix}color-status-info: #{$color-background-info};
  --#{$prefix}color-status-info-hover: #{$color-background-info-hover};
  --#{$prefix}color-status-info-active: #{$color-background-info-active};

  // Icons colors
  --#{$prefix}icon-danger-active: #{$icon-danger-active};
  --#{$prefix}icon-danger-hover: #{$icon-danger-hover};
  --#{$prefix}icon-danger: #{$icon-danger};
  --#{$prefix}icon-warning-active: #{$icon-warning-active};
  --#{$prefix}icon-warning-hover: #{$icon-warning-hover};
  --#{$prefix}icon-warning: #{$icon-warning};
  --#{$prefix}icon-success-active: #{$icon-success-active};
  --#{$prefix}icon-success-hover: #{$icon-success-hover};
  --#{$prefix}icon-success: #{$icon-success};
  --#{$prefix}icon-info-active: #{$icon-info-active};
  --#{$prefix}icon-info-hover: #{$icon-info-hover};
  --#{$prefix}icon-info: #{$icon-info};
  --#{$prefix}icon-secondary-active: #{$icon-secondary-active};
  --#{$prefix}icon-inverse: #{tokens.$it-icon-inverse};
  --#{$prefix}icon-secondary-hover: #{$icon-secondary-hover};
  --#{$prefix}icon-secondary: #{$icon-secondary};
  --#{$prefix}icon-primary-active: #{$icon-primary-active};
  --#{$prefix}icon-primary-hover: #{$icon-primary-hover};
  --#{$prefix}icon-primary: #{$icon-primary};
  --#{$prefix}icon-default: #{tokens.$it-icon-default};
  --#{$prefix}icon-disabled: #{tokens.$it-icon-disabled};
  --#{$prefix}icon-spacing: #{tokens.$it-spacing-xs};

  // Transitions
  --#{$prefix}transition-instant: 0.2s;
}

```



## Variabili di componente

Le variabili CSS dei componenti sono definite all'inizio del relativo codice SCSS nel file `src/scss/components/nome-componente.scss`.

Esempio delle variabili CSS del componente alert:

```scss
// Component: alert
//
// Description: Component styles for alert

.alert {
  --#{$prefix}alert-background-color: var(--#{$prefix}color-background-inverse); // Controls the background color for the alert, using color tokens.
  --#{$prefix}alert-border-color: var(--#{$prefix}color-border-secondary); // Controls the external border color for the alert, using color tokens.
  --#{$prefix}alert-border-size: 0.5rem; // Controls the border size for the alert.
  --#{$prefix}alert-heading-color: var(--#{$prefix}color-text-base); // Controls the heading color for the alert, using color tokens.
  --#{$prefix}alert-icon-spacing: var(--#{$prefix}icon-spacing); // Controls the icon spacing for the alert, using spacing tokens.
  --#{$prefix}alert-spacing-inset: var(--#{$prefix}spacing-s); // Controls the inset spacing for the alert, using spacing tokens.
  --#{$prefix}alert-spacing-inset-extra: var(--#{$prefix}spacing-xxl); // Controls the extra inset spacing for the alert, using spacing tokens.
  --#{$prefix}alert-spacing-outside: var(--#{$prefix}spacing-m); // Controls the outside spacing for the alert, using spacing tokens.
  --#{$prefix}alert-text-color: var(--#{$prefix}color-text-base); // Controls the text color for the alert, using color tokens.
}
```
Nel caso di componenti con varianti, le variabili sono gestite secondo una logica dinamica. 

Le variabili CSS di ciascun componente sono documentate in una tabella **Properties** nella relativa pagina di documentazione.

## Gestire i cambiamenti

Quando si personalizza una variabile CSS, è importante distinguere se la variabile è **dinamica** o **statica**.

Una **variabile statica ha un valore fisso**, mentre il valore di una **variabile dinamica cambia in base a condizioni specifiche**, come breakpoint o classi CSS.

Bootstrap Italia 3 segue la logica per cui una proprietà viene definita una volta sola, mentre il valore ad essa associato può cambiare. È il caso delle variabili dinamiche.


### Variabili Dinamiche

Le variabili dinamiche cambiano valore in base a due condizioni principali:
- un **breakpoint** per il responsive design
- un **selettore** (tag o classe)



#### Variabile dinamica per breakpoint

Ad esempio, la dimensione responsive dei titoli da `h1` a `h6` è gestita esclusivamenteall'interno del file `_root.scss`, cambiando il valore a partire da un breakpoint specifico:

```scss

/* _root.scss */
:root {
  --#{$prefix}heading-1-font-size: #{tokens.$it-heading-1-font-size};
  --#{$prefix}heading-2-font-size: #{tokens.$it-heading-2-font-size};
  --#{$prefix}heading-3-font-size: #{tokens.$it-heading-3-font-size};
  --#{$prefix}heading-4-font-size: #{tokens.$it-heading-4-font-size};
  --#{$prefix}heading-5-font-size: #{tokens.$it-heading-5-font-size};
  --#{$prefix}heading-6-font-size: #{tokens.$it-heading-6-font-size};

  @include media-breakpoint-up(sm) {
    --#{$prefix}heading-1-font-size: #{tokens.$it-heading-1-font-size-l};
    --#{$prefix}heading-2-font-size: #{tokens.$it-heading-2-font-size-l};
    --#{$prefix}heading-3-font-size: #{tokens.$it-heading-3-font-size-l};
    --#{$prefix}heading-4-font-size: #{tokens.$it-heading-4-font-size-l};
    --#{$prefix}heading-5-font-size: #{tokens.$it-heading-5-font-size-l};
    --#{$prefix}heading-6-font-size: #{tokens.$it-heading-6-font-size-l};
  }
}
```

Nel file `_type.scss`, la proprietà `font-size` dei titoli è dichiarata una volta sola per ciascun tag e classe di titolo:

```scss
/* _type.scss */
h1,
.h1 {
  font-size: var(--#{$prefix}heading-1-font-size);
}

h2,
.h2 {
  font-size: var(--#{$prefix}heading-2-font-size);
}
```

#### Variabile dinamica per selettore

Nel caso di cambiamenti che dipendono dall'uso di un selettore (tag o classe) specifico, la variabile cambia valore ad essa assoacito. Ad esempio, lo sfondo di un pulsante con classe `.btn` è trasparente di default, mentre nella variante `.btn-primary` mostra il colore primario:

```scss
/* _buttons.scss */
.btn {
  --#{$prefix}btn-background: transparent; // Controls the background for the button.
}

.btn-primary {
  --#{$prefix}btn-background: var(--#{$prefix}color-background-secondary);;
}
```

Le variabili definite al principio del file SCSS di un componente possono essere ridefinite all'interno dello stesso. Prima di modificarne il valore, verifica se la variabile è statica o dinamica cercando i riferimenti nel codice.