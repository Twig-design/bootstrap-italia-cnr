---
layout: docs
title: Bordi
description: Modifica lo stile di bordi e il loro arrotondamento.
group: organizzare-gli-spazi
toc: true
---

Aggiungi o rimuovi il bordo a un elemento. Puoi scegliere fra un bordo completo oppure un lato alla volta, secondo una
logica aggiuntiva o sottrattiva.

### Aggiuntivo

<div class="bd-example-border-utils">
{% comment %}Example name: Aggiuntivo{% endcomment %}
{% capture example %}
<span class="border"></span>
<span class="border-top"></span>
<span class="border-end"></span>
<span class="border-bottom"></span>
<span class="border-start"></span>
{% endcapture %}{% include example.html content=example %}
</div>

### Sottrattivo

<div class="bd-example-border-utils bd-example-border-utils-0">
{% comment %}Example name: Sottrattivo{% endcomment %}
{% capture example %}
<span class="border-0"></span>
<span class="border-top-0"></span>
<span class="border-end-0"></span>
<span class="border-bottom-0"></span>
<span class="border-start-0"></span>
{% endcapture %}{% include example.html content=example %}
</div>

## Colore dei bordi

Cambia il colore del bordo scegliendo dalla palette del tema utilizzato.

<div class="bd-example-border-utils">
{% comment %}Example name: Varianti di colore{% endcomment %}
{% capture example %}
{% for color in site.data.theme-colors %}
<span class="border border-{{ color.name }}"></span>{% endfor %}
<span class="border border-white"></span>
{% endcapture %}{% include example.html content=example %}
</div>

## Bordi arrotondati

Classi per arrotondare facilmente gli angoli di un elemento.

{% comment %}Example name: Arrotondati{% endcomment %}
{% capture example %}
  <img src="https://placehold.co/75x75/ebebeb/808080/?text=Immagine" class="rounded" alt="Esempio di immagine arrotondata">
  <img src="https://placehold.co/75x75/ebebeb/808080/?text=Immagine" class="rounded-top" alt="Esempio di immagine arrotondata in alto">
  <img src="https://placehold.co/75x75/ebebeb/808080/?text=Immagine" class="rounded-end" alt="Esempio di immagine arrotondata a destra">
  <img src="https://placehold.co/75x75/ebebeb/808080/?text=Immagine" class="rounded-bottom" alt="Esempio di immagine arrotondata in basso">
  <img src="https://placehold.co/75x75/ebebeb/808080/?text=Immagine" class="rounded-start" alt="Esempio di immagine arrotondata a sinistra">
  <img src="https://placehold.co/75x75/ebebeb/808080/?text=Immagine" class="rounded-circle" alt="Esempio di immagine arrotondata a cerchio">
  <img src="https://placehold.co/75x75/ebebeb/808080/?text=Immagine" class="rounded-0" alt="Esempio di immagine non arrotondata (sovrascrive l'eventuale arrotondamento applicato precedentemente)">
  <img src="https://placehold.co/150x75/ebebeb/808080/?text=Immagine" class="rounded-pill" alt="Esempio di immagine arrotondata a pillola">
{% endcapture %}{% include example.html content=example %}

## Arrotondamento brand

Per etichette, immagini e banner con l'angolo superiore destro retto (stile CNR) sono disponibili le classi utility `.rounded-brand-sm`, `.rounded-brand-md` e `.rounded-brand-lg`.

{% capture example %}
<div class="d-flex flex-wrap gap-3 align-items-end">
  <div class="p-4 bg-primary text-white rounded-brand-sm">`.rounded-brand-sm`</div>
  <div class="p-4 bg-primary text-white rounded-brand-md">`.rounded-brand-md`</div>
  <div class="p-4 bg-primary text-white rounded-brand-lg">`.rounded-brand-lg`</div>
</div>
{% endcapture %}{% include example.html content=example %}

I valori sono esposti anche come variabili CSS globali:

| Classe utility | Variabile CSS | Valore |
| -------------- | ------------- | ------ |
| `.rounded-brand-sm` | `--bsi-radius-brand-sm` | `16px 0 16px 16px` |
| `.rounded-brand-md` | `--bsi-radius-brand-md` | `32px 0 32px 32px` |
| `.rounded-brand-lg` | `--bsi-radius-brand-lg` | `48px 0 48px 48px` |
{: .table .table-cols-equal .mb-4}

Per gli altri token di arrotondamento e spessore bordo (`--bsi-radius-smooth`, `--bsi-border-thick`, ecc.) consulta la pagina [Variabili CSS]({{ site.baseurl }}/docs/personalizzare-la-libreria/variabili-css/).