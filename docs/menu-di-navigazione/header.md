---
layout: docs
title: Header
description: Documentazione ed esempi per la creazione di una testata di navigazione.
group: menu-di-navigazione
toc: true
---

<style>
  /* Style override for Documentation purposes */
 .bd-example {
   background-color: #F7F7F9;
 }
 .bg-override {
   fill:#06c !important;
 }
</style>

L'header di un sito CNR è solitamente composto di 4 elementi principali:

- Uno **Slim Header**, una sottile fascia dello stesso colore del tema principale, con selettore lingua e menu “Esplora i siti del CNR”. Gli stili per ente di appartenenza e pulsante Accedi restano disponibili per usi opzionali.
- Un **Header Centrale** che identifica in modo chiaro il sito attraverso logo e titolo, e può contenere un link per effettuare ricerche sul sito.
- Un **Header Nav** dedicato alla navigazione principale (a sinistra) e a link di servizio come News, Eventi, Contatti (a destra tramite `.navbar-secondary`).
- Una fascia **Esplora come** con pulsanti pillola (`.btn.btn-primary.btn-icon`) per i profili di utenza e un eventuale menu Dipartimenti.

{% capture callout %}

#### Accessibilità

Considerando l'importanza dell'Header per la navigazione, si ricorda porre particolare attenzione all'utilizzo della corretta semantica HTML, alle etichette e agli attributi `ARIA`, oltre a validare e testare sempre con utenti il risultato.

Il titolo del sito, "Nome dell'Istituzione" negli esempi, è contenuto in un `<div>` generico e non un tag `<h1>` per evitare conflitti con gli `<h1>` presenti nelle singole pagine. Nel caso in cui la home page fosse priva di un titolo (es: primo contenuto è una ultima notizia in evidenza) si può applicare il tag `<h1>` al titolo dell'header unicamente in quella pagina oppure creare un `h1` nei contenuti principali di pagina con classe `.visually-hidden`. Questa ultima soluzione sarà anche utile a dare focus direttamente al tag `<h1>` laddove siano presenti [skiplinks]({{ site.baseurl }}/docs/menu-di-navigazione/skiplinks/) che permettano agli utenti che navigano da tastiera o con tecnologie assistive di saltare i contenuti dell'Header.

Maggiori dettagli sull'accessibilità del componente **megamenu** nella [relativa pagina]({{site.baseurl}}/docs/menu-di-navigazione/megamenu/).
{% endcapture %}{% include callout.html content=callout type="accessibility" %}

## Slim Header

Lo **Slim Header** mostra azioni globali allineate a destra: selettore lingua e menu “Esplora i siti del CNR”, entrambi gestiti con il componente [dropdown]({{ site.baseurl }}/docs/componenti/dropdown/).  
Restano supportati (ma non usati nell’esempio CNR) l’intestazione ente di appartenenza a sinistra e il pulsante Accedi.

{% comment %}Example name: Slim header{% endcomment %}
{% capture example %}

<div class="it-header-slim-wrapper">
  <div class="container-xxl">
    <div class="row">
      <div class="col-12">
        <div class="it-header-slim-wrapper-content">
          <div class="it-header-slim-right-zone ms-auto">
            <div class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                <span class="visually-hidden">Selezione lingua: lingua selezionata</span>
                <span>ITA</span>
                <svg class="icon d-none d-lg-block" aria-hidden="true"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use></svg>
              </a>
              <div class="dropdown-menu">
                <div class="row">
                  <div class="col-12">
                    <div class="link-list-wrapper">
                      <ul class="link-list">
                        <li><a class="dropdown-item list-item" href="#"><span>ITA <span class="visually-hidden">selezionata</span></span></a></li>
                        <li><a class="dropdown-item list-item" href="#"><span>ENG</span></a></li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                <span>Esplora i siti del CNR</span>
                <svg class="icon d-none d-lg-block" aria-hidden="true"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use></svg>
              </a>
              <div class="dropdown-menu">
                <div class="row">
                  <div class="col-12">
                    <div class="link-list-wrapper">
                      <ul class="link-list">
                        <li><a class="dropdown-item list-item" href="#"><span>Sito istituzionale</span></a></li>
                        <li><a class="dropdown-item list-item" href="#"><span>Portale della ricerca</span></a></li>
                        <li><a class="dropdown-item list-item" href="#"><span>Amministrazione trasparente</span></a></li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

{% endcapture %}{% include example.html content=example %}

#### Zona destra con pulsante Accedi (opzionale)

Per aggiungere un pulsante di _action_ (es. Accedi) nell'elemento `.it-header-slim-right-zone` usare `.it-access-top-wrapper`. Per renderlo _full-responsive_ applicare anche `.btn-full` al `.btn`.

Il modificatore `.btn-full` è disponibile anche con il tema chiaro attivato da `.theme-light`.

{% comment %}Example name: Slim header con pulsante accedi full-responsive{% endcomment %}
{% capture example %}

<div class="it-header-slim-wrapper">
  <div class="container-xxl">
    <div class="row">
      <div class="col-12">
        <div class="it-header-slim-wrapper-content">
          <a class="d-lg-block navbar-brand" href="#">Ente appartenenza</a>
          <div class="it-header-slim-right-zone">
            <div class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                <span class="visually-hidden">Selezione lingua: lingua selezionata</span>
                <span>ITA</span>
                <svg class="icon d-none d-lg-block"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use></svg>
              </a>
              <div class="dropdown-menu">
                <div class="row">
                  <div class="col-12">
                    <div class="link-list-wrapper">
                      <ul class="link-list">
                        <li><a class="dropdown-item list-item" href="#"><span>ITA <span class="visually-hidden">selezionata</span></span></a></li>
                        <li><a class="dropdown-item list-item" href="#"><span>ENG</span></a></li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <a href="#" class="btn btn-primary btn-icon btn-full">
              <span class="rounded-icon">
                <svg class="icon icon-primary">
                  <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-user"></use>
                </svg>
              </span>
              <span class="d-none d-lg-block">Accedi all'area personale</span>
            </a>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
{% endcapture %}{% include example.html content=example %}

### Versione chiara

Per cambiare tema all'header slim è sufficiente aggiungere la classe `theme-light` al tag `<div class="it-header-slim-wrapper">`

{% comment %}Example name: Slim header, variante chiara{% endcomment %}
{% capture example %}

<div class="it-header-slim-wrapper theme-light">
  <div class="container-xxl">
    <div class="row">
      <div class="col-12">
        <div class="it-header-slim-wrapper-content">
          <a class="d-none d-lg-block navbar-brand" href="#">Ente appartenenza</a>
          <div class="nav-mobile">
            <nav aria-label="Navigazione accessoria">
              <a class="it-opener d-lg-none" data-bs-toggle="collapse" href="#menu1b" role="button" aria-expanded="false" aria-controls="menu4">
                <span>Ente appartenenza</span>
                <svg class="icon" aria-hidden="true"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use></svg>
              </a>
              <div class="link-list-wrapper collapse" id="menu1b">
                <ul class="link-list">
                  <li><a class="dropdown-item list-item" href="#">Link 1</a></li>
                  <li><a class="list-item active" href="#" aria-current="page">Link 2 (Attivo)</a></li>
                </ul>
              </div>
            </nav>
          </div>
          <div class="it-header-slim-right-zone">
            <div class="nav-item dropdown">
              <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                <span class="visually-hidden">Selezione lingua: lingua selezionata</span>
                <span>ITA</span>
                <svg class="icon d-none d-lg-block"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use></svg>
              </a>
              <div class="dropdown-menu">
                <div class="row">
                  <div class="col-12">
                    <div class="link-list-wrapper">
                      <ul class="link-list">
                        <li><a class="dropdown-item list-item" href="#"><span>ITA <span class="visually-hidden">selezionata</span></span></a></li>
                        <li><a class="dropdown-item list-item" href="#"><span>ENG</span></a></li>
                      </ul>
                    </div>
                  </div>
                </div>
              </div>
            </div>
            <div class="it-access-top-wrapper">
              <a class="btn btn-primary btn-xs" href="#">Accedi</a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
{% endcapture %}{% include example.html content=example %}

## Header Centrale

**Header Centrale**, per mostrare il logo dell'ente e la sua descrizione, link aggiuntivi ai social media e l'accesso al motore di ricerca, se presente.

{% comment %}Example name: Header centrale{% endcomment %}
{% capture example %}

<div class="it-header-center-wrapper">
  <div class="container-xxl">
    <div class="row">
      <div class="col-12">
        <div class="it-header-center-content-wrapper">
          <div class="it-brand-wrapper">
            <a href="#">
              <svg class="icon" aria-hidden="true">
                <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-pa"></use>
              </svg>
              <div class="it-brand-text">
                <div class="it-brand-title">Nome dell'Istituzione</div>
                <div class="it-brand-tagline d-none d-md-block">Tag line dell'Istituzione</div>
              </div>
            </a>
          </div>
          <div class="it-right-zone">
            <div class="it-socials d-none d-md-flex">
              <span>Seguici su</span>
              <ul>
                <li>
                  <a href="#" aria-label="Facebook" target="_blank">
                    <svg class="icon">
                      <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-facebook"></use>
                    </svg>
                  </a>
                </li>
                <li>
                  <a href="#" aria-label="Github" target="_blank">
                    <svg class="icon">
                      <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-github"></use>
                    </svg>
                  </a>
                </li>
                <li>
                  <a href="#" aria-label="Twitter" target="_blank">
                    <svg class="icon">
                      <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-twitter"></use>
                    </svg>
                  </a>
                </li>
              </ul>
            </div>
            <div class="it-search-wrapper">
              <span class="d-none d-md-block">Cerca</span>
              <a class="search-link rounded-icon" aria-label="Cerca nel sito" href="#">
                <svg class="icon">
                  <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-search"></use>
                </svg>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
{% endcapture %}{% include example.html content=example %}

### Versione compatta

Per utilizzare la versione più compatta in verticale dell'header centrale è sufficiente aggiungere la classe `it-small-header` al tag `<div class="it-header-center-wrapper">`

{% comment %}Example name: Header centrale, variante compatta{% endcomment %}
{% capture example %}

<div class="it-header-center-wrapper it-small-header">
  <div class="container-xxl">
    <div class="row">
      <div class="col-12">
        <div class="it-header-center-content-wrapper">
          <div class="it-brand-wrapper">
            <a href="#">
              <svg class="icon" aria-hidden="true">
                <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-pa"></use>
              </svg>
              <div class="it-brand-text">
                <div class="it-brand-title">Nome dell'Istituzione</div>
                <div class="it-brand-tagline d-none d-md-block">Tag line dell'Istituzione</div>
              </div>
            </a>
          </div>
          <div class="it-right-zone">
            <div class="it-socials d-none d-md-flex">
              <span>Seguici su</span>
              <ul>
                <li>
                  <a href="#" aria-label="Facebook" target="_blank">
                    <svg class="icon">
                      <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-facebook"></use>
                    </svg>
                  </a>
                </li>
                <li>
                  <a href="#" aria-label="Github" target="_blank">
                    <svg class="icon">
                      <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-github"></use>
                    </svg>
                  </a>
                </li>
                <li>
                  <a href="#" aria-label="Twitter" target="_blank">
                    <svg class="icon">
                      <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-twitter"></use>
                    </svg>
                  </a>
                </li>
              </ul>
            </div>
            <div class="it-search-wrapper">
              <span class="d-none d-md-block">Cerca</span>
              <a class="search-link rounded-icon" aria-label="Cerca nel sito" href="#">
                <svg class="icon">
                  <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-search"></use>
                </svg>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
{% endcapture %}{% include example.html content=example %}

### Versione chiara

Per cambiare tema all'header centrale è sufficiente aggiungere la classe `theme-light` al tag `<div class="it-header-center-wrapper">`.

{% comment %}Example name: Header centrale, variante chiara{% endcomment %}
{% capture example %}

<div class="it-header-center-wrapper theme-light">
  <div class="container-xxl">
    <div class="row">
      <div class="col-12">
        <div class="it-header-center-content-wrapper">
          <div class="it-brand-wrapper">
            <a href="#">
              <svg class="icon" aria-hidden="true">
                <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-pa"></use>
              </svg>
              <div class="it-brand-text">
                <div class="it-brand-title">Nome dell'Istituzione</div>
                <div class="it-brand-tagline d-none d-md-block">Tag line dell'Istituzione</div>
              </div>
            </a>
          </div>
          <div class="it-right-zone">
            <div class="it-socials d-none d-md-flex">
              <span>Seguici su</span>
              <ul>
                <li>
                  <a href="#" aria-label="Facebook" target="_blank">
                    <svg class="icon">
                      <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-facebook"></use>
                    </svg>
                  </a>
                </li>
                <li>
                  <a href="#" aria-label="Github" target="_blank">
                    <svg class="icon">
                      <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-github"></use>
                    </svg>
                  </a>
                </li>
                <li>
                  <a href="#" aria-label="Twitter" target="_blank">
                    <svg class="icon">
                      <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-twitter"></use>
                    </svg>
                  </a>
                </li>
              </ul>
            </div>
            <div class="it-search-wrapper">
              <span class="d-none d-md-block">Cerca</span>
              <a class="search-link rounded-icon" aria-label="Cerca nel sito" href="#">
                <svg class="icon">
                  <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-search"></use>
                </svg>
              </a>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>
{% endcapture %}{% include example.html content=example %}

## Header Nav

**Header Nav**, per elencare le voci di navigazione, siano esse semplici link, o pulsanti per [Dropdown]({{ site.baseurl }}/docs/componenti/dropdown/) e [Megamenu]({{ site.baseurl }}/docs/menu-di-navigazione/megamenu/).

{% comment %}Example name: Header navigazione{% endcomment %}
{% capture example %}

<div class="it-header-navbar-wrapper">
  <div class="container-xxl">
    <div class="row">
      <div class="col-12">
        <!--start nav-->
        <nav class="navbar navbar-expand-lg" aria-label="Navigazione principale">
          <button class="custom-navbar-toggler" type="button" aria-controls="nav1" aria-label="Mostra/Nascondi la navigazione" data-bs-toggle="navbarcollapsible" data-bs-target="#nav1">
            <svg class="icon"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-burger"></use></svg>
          </button>
          <div class="navbar-collapsable" id="nav1" tabindex="-1">
            <div class="close-div">
              <button class="btn close-menu" type="button">
                <span class="visually-hidden">Nascondi la navigazione</span>
                <svg class="icon"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-close-big"></use></svg>
              </button>
            </div>
            <div class="menu-wrapper">
              <ul class="navbar-nav">
                <li class="nav-item active"><a class="nav-link active" href="#" aria-current="page"><span>Link attivo</span></a></li>
                <li class="nav-item"><a class="nav-link disabled" href="#" aria-disabled="true"><span>Link disabilitato</span></a></li>
                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false" id="mainNavDropdown1">
                    <span>Dropdown</span>
                    <svg class="icon icon-xs"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use></svg>
                  </a>
                  <div class="dropdown-menu" role="region" aria-labelledby="mainNavDropdown1">
                    <div class="link-list-wrapper">
                      <ul class="link-list">
                        <li><a class="dropdown-item list-item" href="#"><span>Link lista 1</span></a></li>
                        <li><a class="dropdown-item list-item" href="#"><span>Link lista 2</span></a></li>
                        <li><a class="dropdown-item list-item" href="#"><span>Link lista 3</span></a></li>
                        <li><span class="divider"></span></li>
                        <li><a class="dropdown-item list-item" href="#"><span>Link lista 4</span></a></li>
                      </ul>
                    </div>
                  </div>
                </li>
                <!-- megamenu -->
                <li class="nav-item dropdown megamenu">
                  <button type="button" class="nav-link dropdown-toggle px-lg-2 px-xl-3" data-bs-toggle="dropdown" aria-expanded="false" id="megamenu-1" data-focus-mouse="false">
                      <span>Megamenu</span><svg role="img" class="icon icon-xs"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use></svg>
                  </button>
                  <div class="dropdown-menu shadow-lg" role="region" aria-labelledby="megamenu-1">
                    <div class="megamenu-content">
                      <div class="row">
                        <div class="col-xs-12 col-lg-4 px-0">
                          <div class="row">
                            <div class="col-12 it-vertical it-description pb-lg-3">
                              <div class="description-content px-4 ps-sm-5 ms-3">
                                <div class="ratio ratio-21x9 lightgrey-bg-a1 mb-4 rounded">
                                  <figure class="figure">
                                    <img src="https://placehold.co/560x240/ebebeb/808080/?text=Immagine" class="figure-img img-fluid rounded" alt="Segnaposto">
                                  </figure>
                                </div>
                                <p>
                                  Testo utile a fornire una descrizione dei contenuti della sezione <strong>megamenu</strong>.
                                </p>
                              </div>
                            </div>
                          </div>
                        </div>
                        <div class="col-12 col-lg-8">
                          <div class="it-heading-link-wrapper">
                            <a class="it-heading-link" href="#"><svg role="img" class="icon icon-sm me-2 mb-1"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                            <span>Esplora la sezione megamenu</span>
                            </a>
                          </div>
                          <div class="row">
                            <div class="col-12 col-lg-6">
                              <div class="link-list-wrapper">
                                <ul class="link-list">
                                  <li>
                                    <a class="list-item dropdown-item" href="#">
                                      <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                      <span>Link lista 1</span>
                                    </a>
                                  </li>
                                  <li>
                                    <a class="list-item dropdown-item" href="#">
                                      <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                      <span>Link lista 2</span>
                                    </a>
                                  </li>
                                  <li>
                                    <a class="list-item dropdown-item " href="#">
                                      <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                      <span>Link lista 3</span>
                                    </a>
                                  </li>
                                </ul>
                              </div>
                            </div>
                            <div class="col-12 col-lg-6">
                              <div class="link-list-wrapper">
                                <ul class="link-list">
                                  <li>
                                    <a class="list-item dropdown-item" href="#">
                                      <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                      <span>Link lista 4</span>
                                    </a>
                                  </li>
                                  <li>
                                    <a class="list-item dropdown-item" href="#">
                                      <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                      <span>Link lista 5</span>
                                    </a>
                                  </li>
                                  <li>
                                    <a class="list-item dropdown-item " href="#">
                                      <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                      <span>Link lista 6</span>
                                    </a>
                                  </li>
                                </ul>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
    </div>
  </div>
</div>
{% endcapture %}{% include example.html content=example %}

### Temi colore disponibili

I'Header Nav ha due temi colore, uno chiaro ("light") e uno scuro ("dark"). Lo stile di default ha differenti caratteristiche colore a seconda della versione desktop e mobile:

- Su **desktop** lo stile di default ha un **background di colore primario e link bianchi**. Gli elementi **Dropdown** e **Megamenu** hanno background bianco, testi neri e link di colore primario.
- Su **mobile** lo stile di default ha un **background bianco e testi e link di colore primario**.

Per modificare il colore di sfondo e testi di Header Nav bisogna aggiungere la class `.theme-light` al tag `<nav class="it-header-navbar-wrapper">`:

#### Header Nav standard

{% comment %}Example name: Header navigazione standard{% endcomment %}
{% capture example %}

<div class="it-header-navbar-wrapper">
  <div class="container-xxl">
    <div class="row">
      <div class="col-12">
        <!--start nav-->
        <nav class="navbar navbar-expand-lg" aria-label="Navigazione principale">
          <button class="custom-navbar-toggler" type="button" aria-controls="nav0" aria-label="Mostra/Nascondi la navigazione" data-bs-toggle="navbarcollapsible" data-bs-target="#nav0">
            <svg class="icon"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-burger"></use></svg>
          </button>
          <div class="navbar-collapsable" id="nav0" tabindex="-1">
            <div class="close-div">
              <button class="btn close-menu" type="button">
                <span class="visually-hidden">Nascondi la navigazione</span>
                <svg class="icon"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-close-big"></use></svg>
              </button>
            </div>
            <div class="menu-wrapper">
              <ul class="navbar-nav">
                <li class="nav-item active"><a class="nav-link active" href="#" aria-current="page"><span>Link attivo</span></a></li>
                <li class="nav-item"><a class="nav-link disabled" href="#" aria-disabled="true"><span>Link disabilitato</span></a></li>
                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false" id="mainNavDropdown0">
                    <span>Dropdown</span>
                    <svg class="icon icon-xs"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use></svg>
                  </a>
                  <div class="dropdown-menu" role="region" aria-labelledby="mainNavDropdown0">
                    <div class="link-list-wrapper">
                      <ul class="link-list">
                        <li><a class="dropdown-item list-item" href="#"><span>Link lista 1</span></a></li>
                        <li><a class="dropdown-item list-item" href="#"><span>Link lista 2</span></a></li>
                        <li><a class="dropdown-item list-item" href="#"><span>Link lista 3</span></a></li>
                        <li><span class="divider"></span></li>
                        <li><a class="dropdown-item list-item" href="#"><span>Link lista 4</span></a></li>
                      </ul>
                    </div>
                  </div>
                </li>
                <!-- megamenu -->
                <li class="nav-item dropdown megamenu">
                  <button type="button" class="nav-link dropdown-toggle px-lg-2 px-xl-3" data-bs-toggle="dropdown" aria-expanded="false" id="megamenu-2" data-focus-mouse="false">
                      <span>Megamenu</span><svg role="img" class="icon icon-xs"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use></svg>
                  </button>
                  <div class="dropdown-menu shadow-lg" role="region" aria-labelledby="megamenu-2">
                    <div class="megamenu-content">
                      <div class="row">
                        <div class="col-xs-12 col-lg-4 px-0">
                          <div class="row">
                            <div class="col-12 it-vertical it-description pb-lg-3">
                              <div class="description-content px-4 ps-sm-5 ms-3">
                                <div class="ratio ratio-21x9 lightgrey-bg-a1 mb-4 rounded">
                                  <figure class="figure">
                                    <img src="https://placehold.co/560x240/ebebeb/808080/?text=Immagine" class="figure-img img-fluid rounded" alt="Segnaposto">
                                  </figure>
                                </div>
                                <p>
                                  Testo utile a fornire una descrizione dei contenuti della sezione <strong>megamenu</strong>.
                                </p>
                              </div>
                            </div>
                          </div>
                        </div>
                        <div class="col-12 col-lg-8">
                          <div class="it-heading-link-wrapper">
                            <a class="it-heading-link" href="#"><svg role="img" class="icon icon-sm me-2 mb-1"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                            <span>Esplora la sezione megamenu</span>
                            </a>
                          </div>
                          <div class="row">
                            <div class="col-12 col-lg-6">
                              <div class="link-list-wrapper">
                                <ul class="link-list">
                                  <li>
                                    <a class="list-item dropdown-item" href="#">
                                      <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                      <span>Link lista 1</span>
                                    </a>
                                  </li>
                                  <li>
                                    <a class="list-item dropdown-item" href="#">
                                      <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                      <span>Link lista 2</span>
                                    </a>
                                  </li>
                                  <li>
                                    <a class="list-item dropdown-item " href="#">
                                      <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                      <span>Link lista 3</span>
                                    </a>
                                  </li>
                                </ul>
                              </div>
                            </div>
                            <div class="col-12 col-lg-6">
                              <div class="link-list-wrapper">
                                <ul class="link-list">
                                  <li>
                                    <a class="list-item dropdown-item" href="#">
                                      <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                      <span>Link lista 4</span>
                                    </a>
                                  </li>
                                  <li>
                                    <a class="list-item dropdown-item" href="#">
                                      <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                      <span>Link lista 5</span>
                                    </a>
                                  </li>
                                  <li>
                                    <a class="list-item dropdown-item " href="#">
                                      <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                      <span>Link lista 6</span>
                                    </a>
                                  </li>
                                </ul>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
    </div>
  </div>
</div>
{% endcapture %}{% include example.html content=example %}

#### Header Nav - tema chiaro

{% comment %}Example name: Header navigazione desktop chiara{% endcomment %}
{% capture example %}

<div class="it-header-navbar-wrapper theme-light">
  <div class="container-xxl">
    <div class="row">
      <div class="col-12">
        <!--start nav-->
        <nav class="navbar navbar-expand-lg" aria-label="Navigazione principale">
          <button class="custom-navbar-toggler" type="button" aria-controls="nav3" aria-label="Mostra/Nascondi la navigazione" data-bs-toggle="navbarcollapsible" data-bs-target="#nav3">
            <svg class="icon">
              <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-burger"></use>
            </svg>
          </button>
          <div class="navbar-collapsable" id="nav3" tabindex="-1">
            <div class="close-div">
              <button class="btn close-menu" type="button">
                <span class="visually-hidden">Nascondi la navigazione</span>
                <svg class="icon"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-close-big"></use></svg>
              </button>
            </div>
            <div class="menu-wrapper">
              <ul class="navbar-nav">
                <li class="nav-item active"><a class="nav-link active" href="#" aria-current="page"><span>Link attivo</span></a></li>
                <li class="nav-item"><a class="nav-link disabled" href="#" aria-disabled="true"><span>Link disabilitato</span></a></li>
                <li class="nav-item dropdown">
                  <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false" id="mainNavDropdown3">
                    <span>Dropdown</span>
                    <svg class="icon icon-xs"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use></svg>
                  </a>
                  <div class="dropdown-menu" role="region" aria-labelledby="mainNavDropdown3">
                    <div class="link-list-wrapper">
                      <ul class="link-list">
                        <li><a class="dropdown-item list-item" href="#"><span>Link lista 1</span></a></li>
                        <li><a class="dropdown-item list-item" href="#"><span>Link lista 2</span></a></li>
                        <li><a class="dropdown-item list-item" href="#"><span>Link lista 3</span></a></li>
                        <li><span class="divider"></span></li>
                        <li><a class="dropdown-item list-item" href="#"><span>Link lista 4</span></a></li>
                      </ul>
                    </div>
                  </div>
                </li>
                <!-- megamenu -->
                <li class="nav-item dropdown megamenu">
                  <button type="button" class="nav-link dropdown-toggle px-lg-2 px-xl-3" data-bs-toggle="dropdown" aria-expanded="false" id="megamenu-4" data-focus-mouse="false">
                      <span>Megamenu</span><svg role="img" class="icon icon-xs"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use></svg>
                  </button>
                  <div class="dropdown-menu shadow-lg" role="region" aria-labelledby="megamenu-4">
                    <div class="megamenu-content">
                      <div class="row">
                        <div class="col-xs-12 col-lg-4 px-0">
                          <div class="row">
                            <div class="col-12 it-vertical it-description pb-lg-3">
                              <div class="description-content px-4 ps-sm-5 ms-3">
                                <div class="ratio ratio-21x9 lightgrey-bg-a1 mb-4 rounded">
                                  <figure class="figure">
                                    <img src="https://placehold.co/560x240/ebebeb/808080/?text=Immagine" class="figure-img img-fluid rounded" alt="Segnaposto">
                                  </figure>
                                </div>
                                <p>
                                  Testo utile a fornire una descrizione dei contenuti della sezione <strong>megamenu</strong>.
                                </p>
                              </div>
                            </div>
                          </div>
                        </div>
                        <div class="col-12 col-lg-8">
                          <div class="it-heading-link-wrapper">
                            <a class="it-heading-link" href="#"><svg role="img" class="icon icon-sm me-2 mb-1"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                            <span>Esplora la sezione megamenu</span>
                            </a>
                          </div>
                          <div class="row">
                            <div class="col-12 col-lg-6">
                              <div class="link-list-wrapper">
                                <ul class="link-list">
                                  <li>
                                    <a class="list-item dropdown-item" href="#">
                                      <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                      <span>Link lista 1</span>
                                    </a>
                                  </li>
                                  <li>
                                    <a class="list-item dropdown-item" href="#">
                                      <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                      <span>Link lista 2</span>
                                    </a>
                                  </li>
                                  <li>
                                    <a class="list-item dropdown-item " href="#">
                                      <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                      <span>Link lista 3</span>
                                    </a>
                                  </li>
                                </ul>
                              </div>
                            </div>
                            <div class="col-12 col-lg-6">
                              <div class="link-list-wrapper">
                                <ul class="link-list">
                                  <li>
                                    <a class="list-item dropdown-item" href="#">
                                      <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                      <span>Link lista 4</span>
                                    </a>
                                  </li>
                                  <li>
                                    <a class="list-item dropdown-item" href="#">
                                      <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                      <span>Link lista 5</span>
                                    </a>
                                  </li>
                                  <li>
                                    <a class="list-item dropdown-item " href="#">
                                      <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                      <span>Link lista 6</span>
                                    </a>
                                  </li>
                                </ul>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
    </div>
  </div>
</div>
{% endcapture %}{% include example.html content=example %}

#### Navigazione secondaria

Al menu di navigazione principale può essere aggiunto anche un menu di navigazione secondario includendo a `.menu-wrapper` una seconda lista `<ul>` con classe `.navbar-nav.navbar-secondary` e la stessa struttura dati della lista `.navbar-nav` principale.

{% comment %}Example name: Header navigazione secondaria{% endcomment %}
{% capture example %}

<div class="it-header-navbar-wrapper">
  <div class="container-xxl">
    <div class="row">
      <div class="col-12">
        <!--start nav-->
        <nav class="navbar navbar-expand-lg" aria-label="Navigazione principale">
          <button class="custom-navbar-toggler" type="button" aria-controls="nav4" aria-label="Mostra/Nascondi la navigazione" data-bs-toggle="navbarcollapsible" data-bs-target="#nav4">
            <svg class="icon"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-burger"></use></svg>
          </button>
          <div class="navbar-collapsable" id="nav4" tabindex="-1">
            <div class="close-div">
              <button class="btn close-menu" type="button">
                <span class="visually-hidden">Nascondi la navigazione</span>
                <svg class="icon"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-close-big"></use></svg>
              </button>
            </div>
            <div class="menu-wrapper">
              <ul class="navbar-nav">
                <li class="nav-item active"><a class="nav-link active" href="#" aria-current="page"><span>Link attivo</span></a></li>
                <li class="nav-item"><a class="nav-link disabled" href="#" aria-disabled="true"><span>Link disabilitato</span></a></li>
                <li class="nav-item"><a class="nav-link" href="#"><span>Link</span></a></li>
              </ul>
              <ul class="navbar-nav navbar-secondary">
                <li class="nav-item"><a class="nav-link" href="#"><span>Link secondario</span></a></li>
                <li class="nav-item"><a class="nav-link" href="#"><span>Link secondario</span></a></li>
              </ul>
            </div>
          </div>
        </nav>
      </div>
    </div>
  </div>
</div>
{% endcapture %}{% include example.html content=example %}

## Esplora come (audience bar)

Fascia opzionale sotto la navigazione principale. Usa i [pulsanti con icona]({{ site.baseurl }}/docs/componenti/buttons/#pulsanti-con-icona) (`.btn.btn-primary.btn-xs.btn-icon`) come trigger di [dropdown]({{ site.baseurl }}/docs/componenti/dropdown/): sull’header scuro diventano pillole bianche con testo e icona blu chiaro.

{% comment %}Example name: Header audience bar{% endcomment %}
{% capture example %}

<div class="it-header-audience-wrapper">
  <div class="container-xxl">
    <div class="it-header-audience-content">
      <span class="it-header-audience-label">Esplora come:</span>
      <div class="it-header-audience-pills">
        <div class="dropdown">
          <button class="btn btn-primary btn-xs btn-icon" type="button" data-bs-toggle="dropdown" aria-expanded="false" id="docs-audience-cittadinanza">
            <svg class="icon icon-xs" aria-hidden="true"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-user"></use></svg>
            <span>Cittadinanza</span>
          </button>
          <div class="dropdown-menu" aria-labelledby="docs-audience-cittadinanza">
            <div class="link-list-wrapper">
              <ul class="link-list">
                <li>
                  <a class="list-item dropdown-item" href="#">
                    <svg class="icon icon-sm me-2" aria-hidden="true"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                    <span>Mostre e musei scientifici</span>
                  </a>
                </li>
                <li>
                  <a class="list-item dropdown-item" href="#">
                    <svg class="icon icon-sm me-2" aria-hidden="true"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                    <span>Scienza per i cittadini</span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="dropdown">
          <button class="btn btn-primary btn-xs btn-icon" type="button" data-bs-toggle="dropdown" aria-expanded="false" id="docs-audience-ricercatori">
            <svg class="icon icon-xs" aria-hidden="true"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-user"></use></svg>
            <span>Ricercatori</span>
          </button>
          <div class="dropdown-menu" aria-labelledby="docs-audience-ricercatori">
            <div class="link-list-wrapper">
              <ul class="link-list">
                <li>
                  <a class="list-item dropdown-item" href="#">
                    <svg class="icon icon-sm me-2" aria-hidden="true"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                    <span>Opportunità di ricerca</span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
        <div class="dropdown">
          <button class="btn btn-primary btn-xs btn-icon" type="button" data-bs-toggle="dropdown" aria-expanded="false" id="docs-audience-pa">
            <svg class="icon icon-xs" aria-hidden="true"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-pa"></use></svg>
            <span>PA</span>
          </button>
          <div class="dropdown-menu" aria-labelledby="docs-audience-pa">
            <div class="link-list-wrapper">
              <ul class="link-list">
                <li>
                  <a class="list-item dropdown-item" href="#">
                    <svg class="icon icon-sm me-2" aria-hidden="true"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                    <span>Servizi per la PA</span>
                  </a>
                </li>
              </ul>
            </div>
          </div>
        </div>
      </div>
      <div class="it-header-audience-extra">
        <div class="dropdown">
          <a class="dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
            <img class="it-header-audience-dept-logo" src="{{site.baseurl}}/docs/assets/img/icons/cnr_logo.png" alt="" width="48" height="43" aria-hidden="true">
            <span>I dipartimenti</span>
            <svg class="icon" aria-hidden="true"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use></svg>
          </a>
          <div class="dropdown-menu dropdown-menu-end">
            <div class="link-list-wrapper">
              <ul class="link-list">
                <li><a class="dropdown-item list-item" href="#"><span>Scienze fisiche</span></a></li>
                <li><a class="dropdown-item list-item" href="#"><span>Scienze chimiche</span></a></li>
              </ul>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</div>

{% endcapture %}{% include example.html content=example %}

## Header Completa

{% comment %}Example name: Header completa{% endcomment %}
{% capture example %}

<header class="it-header-wrapper">
  <div class="it-header-slim-wrapper">
    <div class="container-xxl">
      <div class="row">
        <div class="col-12">
          <div class="it-header-slim-wrapper-content">
            <a class="d-none d-lg-block navbar-brand" href="#">Ente appartenenza</a>
            <div class="nav-mobile">
              <nav aria-label="Navigazione secondaria">
                <a class="it-opener d-lg-none" data-bs-toggle="collapse" href="#menuC1" role="button" aria-expanded="false" aria-controls="menuC1">
                  <span>Ente appartenenza</span>
                  <svg class="icon" aria-hidden="true"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use></svg>
                </a>
                <div class="link-list-wrapper collapse" id="menuC1">
                  <ul class="link-list">
                    <li><a class="dropdown-item list-item" href="#">Link 1</a></li>
                    <li><a class="list-item active" href="#" aria-current="page">Link 2 (Attivo)</a></li>
                  </ul>
                </div>
              </nav>
            </div>
            <div class="it-header-slim-right-zone">
              <div class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  <span class="visually-hidden">Selezione lingua: lingua selezionata</span>
                  <span>ITA</span>
                  <svg class="icon d-none d-lg-block"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use></svg>
                </a>
                <div class="dropdown-menu">
                  <div class="row">
                    <div class="col-12">
                      <div class="link-list-wrapper">
                        <ul class="link-list">
                          <li><a class="dropdown-item list-item" href="#"><span>ITA <span class="visually-hidden">selezionata</span></span></a></li>
                          <li><a class="dropdown-item list-item" href="#"><span>ENG</span></a></li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="it-access-top-wrapper">
                <a class="btn btn-primary btn-xs" href="#">Accedi</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="it-nav-wrapper">
    <div class="it-header-center-wrapper">
      <div class="container-xxl">
        <div class="row">
          <div class="col-12">
            <div class="it-header-center-content-wrapper">
              <div class="it-brand-wrapper">
                <a href="#">
                  <svg class="icon" aria-hidden="true"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-pa"></use></svg>
                  <div class="it-brand-text">
                    <div class="it-brand-title">Nome dell'Istituzione</div>
                    <div class="it-brand-tagline d-none d-md-block">Tag line dell'Istituzione</div>
                  </div>
                </a>
              </div>
              <div class="it-right-zone">
                <div class="it-socials d-none d-md-flex">
                  <span>Seguici su</span>
                  <ul>
                    <li>
                      <a href="#" aria-label="Facebook" target="_blank">
                        <svg class="icon"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-facebook"></use></svg>
                      </a>
                    </li>
                    <li>
                      <a href="#" aria-label="Github" target="_blank">
                        <svg class="icon"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-github"></use></svg>
                      </a>
                    </li>
                    <li>
                      <a href="#" aria-label="Twitter" target="_blank">
                        <svg class="icon"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-twitter"></use></svg>
                      </a>
                    </li>
                  </ul>
                </div>
                <div class="it-search-wrapper">
                  <span class="d-none d-md-block">Cerca</span>
                  <a class="search-link rounded-icon" aria-label="Cerca nel sito" href="#">
                    <svg class="icon"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-search"></use></svg>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="it-header-navbar-wrapper">
      <div class="container-xxl">
        <div class="row">
          <div class="col-12">
            <!--start nav-->
            <nav class="navbar navbar-expand-lg" aria-label="Navigazione principale">
              <button class="custom-navbar-toggler" type="button" aria-controls="navC1" aria-label="Mostra/Nascondi la navigazione" data-bs-toggle="navbarcollapsible" data-bs-target="#navC1">
                <svg class="icon">
                  <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-burger"></use>
                </svg>
              </button>
              <div class="navbar-collapsable" id="navC1" tabindex="-1">
                <div class="close-div">
                  <button class="btn close-menu" type="button">
                    <span class="visually-hidden">Nascondi la navigazione</span>
                    <svg class="icon">
                      <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-close-big"></use>
                    </svg>
                  </button>
                </div>
                <div class="menu-wrapper">
                  <ul class="navbar-nav">
                    <li class="nav-item active"><a class="nav-link active" href="#" aria-current="page"><span>Link attivo</span></a></li>
                    <li class="nav-item"><a class="nav-link disabled" href="#" aria-disabled="true"><span>Link disabilitato</span></a></li>
                    <li class="nav-item dropdown">
                      <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false" id="mainNavDropdownC1">
                        <span>Dropdown</span>
                        <svg class="icon icon-xs">
                          <use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use>
                        </svg>
                      </a>
                      <div class="dropdown-menu" role="region" aria-labelledby="mainNavDropdownC1">
                        <div class="link-list-wrapper">
                          <ul class="link-list">
                            <li><a class="dropdown-item list-item" href="#"><span>Link lista 1</span></a></li>
                            <li><a class="dropdown-item list-item" href="#"><span>Link lista 2</span></a></li>
                            <li><a class="dropdown-item list-item" href="#"><span>Link lista 3</span></a></li>
                            <li><span class="divider"></span></li>
                            <li><a class="dropdown-item list-item" href="#"><span>Link lista 4</span></a></li>
                          </ul>
                        </div>
                      </div>
                    </li>
                    <!-- megamenu -->
                    <li class="nav-item dropdown megamenu">
                      <button type="button" class="nav-link dropdown-toggle px-lg-2 px-xl-3" data-bs-toggle="dropdown" aria-expanded="false" id="megamenu-5" data-focus-mouse="false">
                          <span>Megamenu</span><svg role="img" class="icon icon-xs"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use></svg>
                      </button>
                      <div class="dropdown-menu shadow-lg" role="region" aria-labelledby="megamenu-5">
                        <div class="megamenu-content">
                          <div class="row">
                            <div class="col-xs-12 col-lg-4 px-0">
                              <div class="row">
                                <div class="col-12 it-vertical it-description pb-lg-3">
                                  <div class="description-content px-4 ps-sm-5 ms-3">
                                    <div class="ratio ratio-21x9 lightgrey-bg-a1 mb-4 rounded">
                                      <figure class="figure">
                                        <img src="https://placehold.co/560x240/ebebeb/808080/?text=Immagine" class="figure-img img-fluid rounded" alt="Segnaposto">
                                      </figure>
                                    </div>
                                    <p>
                                      Testo utile a fornire una descrizione dei contenuti della sezione <strong>megamenu</strong>.
                                    </p>
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="col-12 col-lg-8">
                              <div class="it-heading-link-wrapper">
                                <a class="it-heading-link" href="#"><svg role="img" class="icon icon-sm me-2 mb-1"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                <span>Esplora la sezione megamenu</span>
                                </a>
                              </div>
                              <div class="row">
                                <div class="col-12 col-lg-6">
                                  <div class="link-list-wrapper">
                                    <ul class="link-list">
                                      <li>
                                        <a class="list-item dropdown-item" href="#">
                                          <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                          <span>Link lista 1</span>
                                        </a>
                                      </li>
                                      <li>
                                        <a class="list-item dropdown-item" href="#">
                                          <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                          <span>Link lista 2</span>
                                        </a>
                                      </li>
                                      <li>
                                        <a class="list-item dropdown-item " href="#">
                                          <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                          <span>Link lista 3</span>
                                        </a>
                                      </li>
                                    </ul>
                                  </div>
                                </div>
                                <div class="col-12 col-lg-6">
                                  <div class="link-list-wrapper">
                                    <ul class="link-list">
                                      <li>
                                        <a class="list-item dropdown-item" href="#">
                                          <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                          <span>Link lista 4</span>
                                        </a>
                                      </li>
                                      <li>
                                        <a class="list-item dropdown-item" href="#">
                                          <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                          <span>Link lista 5</span>
                                        </a>
                                      </li>
                                      <li>
                                        <a class="list-item dropdown-item " href="#">
                                          <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                          <span>Link lista 6</span>
                                        </a>
                                      </li>
                                    </ul>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
            </nav>
          </div>
        </div>
      </div>
    </div>
  </div>
</header>

{% endcapture %}{% include example.html content=example %}

### Versione chiara

Nella versione light è consigliabile aggiungere la classe `.it-shadow` al tag `<div class="it-header-wrapper">`.  
Verrà creata un'ombra per enfatizzare l'Header rispetto alla pagina in cui è contenuto.

{% comment %}Example name: Header completa, variante chiara{% endcomment %}
{% capture example %}

<header class="it-header-wrapper it-shadow">
  <div class="it-header-slim-wrapper theme-light">
    <div class="container-xxl">
      <div class="row">
        <div class="col-12">
          <div class="it-header-slim-wrapper-content">
            <a class="d-none d-lg-block navbar-brand" href="#">Ente appartenenza</a>
            <div class="nav-mobile">
              <nav aria-label="Navigazione secondaria">
                <a class="it-opener d-lg-none" data-bs-toggle="collapse" href="#menuC2" role="button" aria-expanded="false" aria-controls="menuC2">
                  <span>Ente appartenenza</span>
                  <svg class="icon" aria-hidden="true"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use></svg>
                </a>
                <div class="link-list-wrapper collapse" id="menuC2">
                  <ul class="link-list">
                    <li><a class="dropdown-item list-item" href="#">Link 1</a></li>
                    <li><a class="list-item active" href="#" aria-current="page">Link 2 (Attivo)</a></li>
                  </ul>
                </div>
              </nav>
            </div>
            <div class="it-header-slim-right-zone">
              <div class="nav-item dropdown">
                <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false">
                  <span class="visually-hidden">Selezione lingua: lingua selezionata</span>
                  <span>ITA</span>
                  <svg class="icon d-none d-lg-block"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use></svg>
                </a>
                <div class="dropdown-menu">
                  <div class="row">
                    <div class="col-12">
                      <div class="link-list-wrapper">
                        <ul class="link-list">
                          <li><a class="dropdown-item list-item" href="#"><span>ITA <span class="visually-hidden">selezionata</span></span></a></li>
                          <li><a class="dropdown-item list-item" href="#"><span>ENG</span></a></li>
                        </ul>
                      </div>
                    </div>
                  </div>
                </div>
              </div>
              <div class="it-access-top-wrapper">
                <a class="btn btn-primary btn-xs" href="#">Accedi</a>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
  <div class="it-nav-wrapper">
    <div class="it-header-center-wrapper theme-light">
      <div class="container-xxl">
        <div class="row">
          <div class="col-12">
            <div class="it-header-center-content-wrapper">
              <div class="it-brand-wrapper">
                <a href="#">
                  <svg class="icon" aria-hidden="true"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-pa"></use></svg>
                  <div class="it-brand-text">
                    <div class="it-brand-title">Nome dell'Istituzione</div>
                    <div class="it-brand-tagline d-none d-md-block">Tag line dell'Istituzione</div>
                  </div>
                </a>
              </div>
              <div class="it-right-zone">
                <div class="it-socials d-none d-md-flex">
                  <span>Seguici su</span>
                  <ul>
                    <li>
                      <a href="#" aria-label="Facebook" target="_blank">
                        <svg class="icon"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-facebook"></use></svg>
                      </a>
                    </li>
                    <li>
                      <a href="#" aria-label="Github" target="_blank">
                        <svg class="icon"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-github"></use></svg>
                      </a>
                    </li>
                    <li>
                      <a href="#" aria-label="Twitter" target="_blank">
                        <svg class="icon"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-twitter"></use></svg>
                      </a>
                    </li>
                  </ul>
                </div>
                <div class="it-search-wrapper">
                  <span class="d-none d-md-block">Cerca</span>
                  <a class="search-link rounded-icon" aria-label="Cerca nel sito" href="#">
                    <svg class="icon"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-search"></use></svg>
                  </a>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
    <div class="it-header-navbar-wrapper theme-light">
      <div class="container-xxl">
        <div class="row">
          <div class="col-12">
            <!--start nav-->
            <nav class="navbar navbar-expand-lg" aria-label="Navigazione principale">
              <button class="custom-navbar-toggler" type="button" aria-controls="navC2" aria-label="Mostra/Nascondi la navigazione" data-bs-toggle="navbarcollapsible" data-bs-target="#navC2">
                <svg class="icon"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-burger"></use></svg>
              </button>
              <div class="navbar-collapsable" id="navC2" tabindex="-1">
                <div class="close-div">
                  <button class="btn close-menu" type="button">
                    <span class="visually-hidden">Nascondi la navigazione</span>
                    <svg class="icon"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-close-big"></use></svg>
                  </button>
                </div>
                <div class="menu-wrapper">
                  <ul class="navbar-nav">
                    <li class="nav-item active"><a class="nav-link active" href="#" aria-current="page"><span>Link attivo</span></a></li>
                    <li class="nav-item"><a class="nav-link disabled" href="#" aria-disabled="true"><span>Link disabilitato</span></a></li>
                    <li class="nav-item dropdown">
                      <a class="nav-link dropdown-toggle" href="#" role="button" data-bs-toggle="dropdown" aria-expanded="false" id="mainNavDropdownC2">
                        <span>Dropdown</span>
                        <svg class="icon icon-xs"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use></svg>
                      </a>
                      <div class="dropdown-menu" role="region" aria-labelledby="mainNavDropdownC2">
                        <div class="link-list-wrapper">
                          <ul class="link-list">
                            <li><a class="dropdown-item list-item" href="#"><span>Link lista 1</span></a></li>
                            <li><a class="dropdown-item list-item" href="#"><span>Link lista 2</span></a></li>
                            <li><a class="dropdown-item list-item" href="#"><span>Link lista 3</span></a></li>
                            <li><span class="divider"></span></li>
                            <li><a class="dropdown-item list-item" href="#"><span>Link lista 4</span></a></li>
                          </ul>
                        </div>
                      </div>
                    </li>
                    <!-- megamenu -->
                    <li class="nav-item dropdown megamenu">
                      <button type="button" class="nav-link dropdown-toggle px-lg-2 px-xl-3" data-bs-toggle="dropdown" aria-expanded="false" id="megamenu-6" data-focus-mouse="false">
                          <span>Megamenu</span><svg role="img" class="icon icon-xs"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-expand"></use></svg>
                      </button>
                      <div class="dropdown-menu shadow-lg" role="region" aria-labelledby="megamenu-6">
                        <div class="megamenu-content">
                          <div class="row">
                            <div class="col-xs-12 col-lg-4 px-0">
                              <div class="row">
                                <div class="col-12 it-vertical it-description pb-lg-3">
                                  <div class="description-content px-4 ps-sm-5 ms-3">
                                    <div class="ratio ratio-21x9 lightgrey-bg-a1 mb-4 rounded">
                                      <figure class="figure">
                                        <img src="https://placehold.co/560x240/ebebeb/808080/?text=Immagine" class="figure-img img-fluid rounded" alt="Segnaposto">
                                      </figure>
                                    </div>
                                    <p>
                                      Testo utile a fornire una descrizione dei contenuti della sezione <strong>megamenu</strong>.
                                    </p>
                                  </div>
                                </div>
                              </div>
                            </div>
                            <div class="col-12 col-lg-8">
                              <div class="it-heading-link-wrapper">
                                <a class="it-heading-link" href="#"><svg role="img" class="icon icon-sm me-2 mb-1"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                <span>Esplora la sezione megamenu</span>
                                </a>
                              </div>
                              <div class="row">
                                <div class="col-12 col-lg-6">
                                  <div class="link-list-wrapper">
                                    <ul class="link-list">
                                      <li>
                                        <a class="list-item dropdown-item" href="#">
                                          <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                          <span>Link lista 1</span>
                                        </a>
                                      </li>
                                      <li>
                                        <a class="list-item dropdown-item" href="#">
                                          <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                          <span>Link lista 2</span>
                                        </a>
                                      </li>
                                      <li>
                                        <a class="list-item dropdown-item " href="#">
                                          <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                          <span>Link lista 3</span>
                                        </a>
                                      </li>
                                    </ul>
                                  </div>
                                </div>
                                <div class="col-12 col-lg-6">
                                  <div class="link-list-wrapper">
                                    <ul class="link-list">
                                      <li>
                                        <a class="list-item dropdown-item" href="#">
                                          <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                          <span>Link lista 4</span>
                                        </a>
                                      </li>
                                      <li>
                                        <a class="list-item dropdown-item" href="#">
                                          <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                          <span>Link lista 5</span>
                                        </a>
                                      </li>
                                      <li>
                                        <a class="list-item dropdown-item " href="#">
                                          <svg role="img" class="icon icon-sm me-2"><use href="{{site.baseurl}}/dist/svg/sprites.svg#it-arrow-right-triangle"></use></svg>
                                          <span>Link lista 6</span>
                                        </a>
                                      </li>
                                    </ul>
                                  </div>
                                </div>
                              </div>
                            </div>
                          </div>
                        </div>
                      </div>
                    </li>
                  </ul>
                </div>
              </div>
            </nav>
          </div>
        </div>
      </div>
    </div>
  </div>
</header>
{% endcapture %}{% include example.html content=example %}

## Attivazione tramite codice

L'unica funzionalità del componente `Header` che necessita l'attivazione tramite
codice è quella in cui si desidera che lo stesso si comporti in maniera `sticky`
ovvero con la testata sempre visibile in formato ridotto anche allo scorrere
della pagina.

{% include callout-bundle-methods.md %}

### Inizializzazione automatica

Per rendere `sticky` il componente `Header` automaticamente, è sufficiente
utilizzare la classe `.it-header-sticky` nell'elemento identificato con la
classe `.it-header-wrapper` insieme all'attributo `data-bs-toggle="sticky"`.

```html
<div class="it-header-wrapper it-header-sticky" data-bs-toggle="sticky" data-bs-position-type="fixed" data-bs-sticky-class-name="is-sticky">...</div>
```

Per maggiori informazioni e ulteriori opzioni vedere il componente [Sticky]({{ site.baseurl }}/docs/componenti/sticky/) e l'[esempio]({{ site.baseurl }}/docs/esempi/navscroll/).

### Inizializzazione manuale

Il componente `Header` solitamente contiene al suo interno i componenti `Dropdown`,
`NavScroll` e `Collapse`, si rimanda alle sezioni specifiche per l'attivazione di questi componenti:

- [Attivazione Dropdown tramite codice]({{ site.baseurl }}/docs/componenti/dropdown/#attivazione-tramite-codice)
- [Attivazione Collapse tramite codice]({{ site.baseurl }}/docs/componenti/collapse/#attivazione-tramite-codice)
- [Attivazione NavScroll tramite codice]({{ site.baseurl }}/docs/menu-di-navigazione/navscroll/#attivazione-tramite-codice)

Per rendere `sticky` il componente `Header` è possibile inizializzare il
componente manualmente utilizzando la classe `HeaderSticky`:

```js
import { HeaderSticky } from 'bootstrap-italia'

const headerStickyElement = document.querySelector('#myHeaderSticky')
const headerSticky = new HeaderSticky(headerStickyElement)
```

#### Metodi

<div class="table-responsive">
  <table class="table table-bordered table-striped">
    <thead>
      <tr>
        <th style="width: 150px;">Metodo</th>
        <th>Descrizione</th>
      </tr>
    </thead>
    <tbody>
      {% include standard-methods.html class="HeaderSticky" %}
    </tbody>
  </table>
</div>

## Breaking change

{% capture callout %}
- Rimossa la variante `theme-light-desk` per Header Nav, ora è possibile impostare il tema chiaro con la class `.theme-light` al tag `<nav class="it-header-navbar-wrapper">`.
- Cambiata la dimensione del pulsante Accedi: cambiato classe da `.btn-sm` a `.btn-sx`.
- Rimossa la classe `.ms-1` dall'icona `<svg>` che segue la voce Megamenu negli esempi.
{% endcapture %}{% include callout-breaking.html content=callout version="3.0.0" type="danger" %}

{% capture callout %}
La navbar presente negli esempi, quando aperta in versione mobile o a forte ingrandimento, è stata reimplementata come modale per migliorare l'accessibilità con le combinazioni principali di lettori di schermo, sistema operativo e browser. Modifiche principali:

- struttura: la navbar ora utilizza un pattern dialog con backdrop
- gerarchia visiva: la gestione `z-index` è allineata al componente modale
- gestione del focus: implementato `focus-trap.js` per utenti da tastiera e lettori di schermo, e gestione inert
- il comportamento è diverso se implementata dentro o fuori dall'elemento `main` di pagina (se presente)

Se hai personalizzato il CSS della navbar, rivedi le tue modifiche per verificarne la compatibilità. Se hai modificato il comportamento JavaScript, assicurati che funzioni con il nuovo pattern dialog. Testa la tua implementazione con lettori di schermo e con utenti per verificarne l'accessibilità.
{% endcapture %}{% include callout-breaking.html content=callout version="2.15.0" type="danger" %}

{% capture callout %}

- Il toggle del dropdown diventa `<button>` invece di `<a>`.
- Gli altri elementi `<a>` che si comportano come toggle dropdown (eg. scelta Lingua), hanno l'aggiunta dell'attributo `role="button"`.
- Il markup del Megamenu cambia come nel nuovo componente, per approfondire andare alla [relativa pagina]({{site.baseurl}}/docs/menu-di-navigazione/megamenu/).
  {% endcapture %}{% include callout-breaking.html content=callout version="2.8.0" type="danger" %}

{% include properties.md properties=site.data.cprops.header %}
