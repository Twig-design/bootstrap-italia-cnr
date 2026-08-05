---
layout: docs
title: Footer
description: Documentazione ed esempi per la creazione di piè di pagina di navigazione.
group: menu-di-navigazione
toc: true
---

## Introduzione
Il **footer** (in italiano piè di pagina o piede di pagina) è una sezione che contiene tutte le informazioni inerenti al sito web e all’organizzazione che rappresenta.

Per un sito CNR tipicamente include il **logo**, i **contatti**, i link di **menu** e **dipartimenti**, i **profili social** e i link utili in fascia inferiore (privacy, accessibilità, ecc.).

## Footer completo

Nel footer completo sono presenti i seguenti elementi:
- **Logo** dell’ente;
- **Contatti** dell’ente (indirizzo, codice fiscale, P. IVA, PEC);
- **Menu** di navigazione principale;
- **Dipartimenti**;
- **Profili social**, social media policy, 5x1000 e canali RSS;
- **Link utili** in fascia inferiore (Media policy, Note legali, Privacy policy, Mappa del sito, Dichiarazione di accessibilità).

{% comment %}Example name: Completo{% endcomment %}
{% capture example %}
<footer class="it-footer">
  <div class="it-footer-main">
    <div class="container">
      <section class="pb-4">
        <div class="row clearfix">
          <div class="col-sm-12">
            <div class="it-brand-wrapper">
              <a href="#">
                <img class="it-brand-logo" src="{{ site.baseurl }}/docs/assets/img/icons/logo-cnr.svg" alt="Consiglio Nazionale delle Ricerche" width="202" height="47">
              </a>
            </div>
          </div>
        </div>
      </section>
      <section class="pt-4 border-white border-top">
        <div class="row">
          <div class="col-lg-3 col-md-6 pb-3">
            <h4>Contatti</h4>
            <p class="mb-3">
              Consiglio Nazionale delle Ricerche<br>
              Piazzale Aldo Moro, 7 - 00185 Roma, Italia<br>
              Codice Fiscale 80054330586<br>
              Partita IVA 02118311006
            </p>
            <p class="mb-0">
              Indirizzo Posta Elettronica Certificata (PEC) istituzionale<br>
              <a href="mailto:protocollo-ammcen@pec.cnr.it">protocollo-ammcen@pec.cnr.it</a>
            </p>
          </div>
          <div class="col-lg-3 col-md-6 pb-3">
            <h4>Menu</h4>
            <div class="link-list-wrapper">
              <ul class="footer-list link-list clearfix">
                <li><a class="list-item" href="#">Il CNR</a></li>
                <li><a class="list-item" href="#">La ricerca CNR</a></li>
                <li><a class="list-item" href="#">Diffondere la ricerca</a></li>
                <li><a class="list-item" href="#">Valorizzare la ricerca</a></li>
                <li><a class="list-item" href="#">Collaborare</a></li>
                <li><a class="list-item" href="#">News &amp; Eventi</a></li>
                <li><a class="list-item" href="#">Contatti</a></li>
              </ul>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 pb-3">
            <h4>Dipartimenti</h4>
            <div class="link-list-wrapper">
              <ul class="footer-list link-list clearfix">
                <li><a class="list-item" href="#">Fisica e Materia</a></li>
                <li><a class="list-item" href="#">Terra e Ambiente</a></li>
                <li><a class="list-item" href="#">Ingegneria, ICT, Energia e Trasporti</a></li>
                <li><a class="list-item" href="#">Scienze BioMediche</a></li>
                <li><a class="list-item" href="#">Scienze Umane e Sociali</a></li>
                <li><a class="list-item" href="#">Chimica e Tecnologia dei Materiali</a></li>
                <li><a class="list-item" href="#">Bio e Agroalimentare</a></li>
              </ul>
            </div>
          </div>
          <div class="col-lg-3 col-md-6 pb-3">
            <h4>Seguici su</h4>
            <ul class="list-inline text-left social mb-3">
              <li class="list-inline-item">
                <a class="p-2 text-white" href="#"><svg class="icon icon-sm icon-inverse align-top" aria-hidden="true"><use href="{{ site.baseurl }}/dist/svg/sprites.svg#it-facebook"></use></svg><span class="visually-hidden">Facebook (link esterno)</span></a>
              </li>
              <li class="list-inline-item">
                <a class="p-2 text-white" href="#"><svg class="icon icon-sm icon-inverse align-top" aria-hidden="true"><use href="{{ site.baseurl }}/dist/svg/sprites.svg#it-instagram"></use></svg><span class="visually-hidden">Instagram (link esterno)</span></a>
              </li>
              <li class="list-inline-item">
                <a class="p-2 text-white" href="#"><svg class="icon icon-sm icon-inverse align-top" aria-hidden="true"><use href="{{ site.baseurl }}/dist/svg/sprites.svg#it-twitter"></use></svg><span class="visually-hidden">X (link esterno)</span></a>
              </li>
              <li class="list-inline-item">
                <a class="p-2 text-white" href="#"><svg class="icon icon-sm icon-inverse align-top" aria-hidden="true"><use href="{{ site.baseurl }}/dist/svg/sprites.svg#it-whatsapp"></use></svg><span class="visually-hidden">WhatsApp (link esterno)</span></a>
              </li>
              <li class="list-inline-item">
                <a class="p-2 text-white" href="#"><svg class="icon icon-sm icon-inverse align-top" aria-hidden="true"><use href="{{ site.baseurl }}/dist/svg/sprites.svg#it-linkedin"></use></svg><span class="visually-hidden">LinkedIn (link esterno)</span></a>
              </li>
            </ul>
            <div class="link-list-wrapper mb-3">
              <ul class="footer-list link-list clearfix">
                <li><a class="list-item" href="#">Social media policy</a></li>
                <li><a class="list-item fw-bold" href="#">Devolvi il 5x1000 al CNR</a></li>
              </ul>
            </div>
            <h4 class="mb-2">Canali RSS</h4>
            <a class="p-2 text-white" href="#"><svg class="icon icon-sm icon-inverse align-top" aria-hidden="true"><use href="{{ site.baseurl }}/dist/svg/sprites.svg#it-rss"></use></svg><span class="visually-hidden">Canali RSS</span></a>
          </div>
        </div>
      </section>
    </div>
  </div>
  <div class="it-footer-small-prints clearfix">
    <div class="container">
      <ul class="it-footer-small-prints-list list-inline mb-0 d-flex flex-column flex-md-row">
        <li class="list-inline-item"><a href="#">Media Policy</a></li>
        <li class="list-inline-item"><a href="#">Note Legali</a></li>
        <li class="list-inline-item"><a href="#">Privacy Policy</a></li>
        <li class="list-inline-item"><a href="#">Mappa del sito</a></li>
        <li class="list-inline-item"><a href="https://form.agid.gov.it/view/xyz">Dichiarazione Accessibilità <span class="visually-hidden">(link esterno su sito AgID)</span></a></li>
      </ul>
    </div>
  </div>
</footer>
{% endcapture %}{% include example.html content=example %}

## Footer compatto
Il footer compatto è una versione semplificata del footer completo.

Contiene logo, contatti, social e i link utili in fascia inferiore. Può essere utilizzato quando non è necessario mostrare menu e dipartimenti.

{% comment %}Example name: Compatto{% endcomment %}
{% capture example %}
<footer class="it-footer">
  <div class="it-footer-main">
    <div class="container">
      <section class="pb-4">
        <div class="row clearfix">
          <div class="col-sm-12">
            <div class="it-brand-wrapper">
              <a href="#">
                <img class="it-brand-logo" src="{{ site.baseurl }}/docs/assets/img/icons/logo-cnr.svg" alt="Consiglio Nazionale delle Ricerche" width="202" height="47">
              </a>
            </div>
          </div>
        </div>
      </section>
      <section class="pt-4 border-white border-top">
        <div class="row">
          <div class="col-lg-6 col-md-6 mt-2">
            <h4>Contatti</h4>
            <p class="mb-3">
              Consiglio Nazionale delle Ricerche<br>
              Piazzale Aldo Moro, 7 - 00185 Roma, Italia<br>
              Codice Fiscale 80054330586<br>
              Partita IVA 02118311006
            </p>
            <p class="mb-0">
              Indirizzo Posta Elettronica Certificata (PEC) istituzionale<br>
              <a href="mailto:protocollo-ammcen@pec.cnr.it">protocollo-ammcen@pec.cnr.it</a>
            </p>
          </div>
          <div class="col-lg-6 col-md-6 mt-2">
            <h4>Seguici su</h4>
            <ul class="list-inline text-left social mb-3">
              <li class="list-inline-item">
                <a class="p-2 text-white" href="#"><svg class="icon icon-sm icon-inverse align-top" aria-hidden="true"><use href="{{ site.baseurl }}/dist/svg/sprites.svg#it-facebook"></use></svg><span class="visually-hidden">Facebook (link esterno)</span></a>
              </li>
              <li class="list-inline-item">
                <a class="p-2 text-white" href="#"><svg class="icon icon-sm icon-inverse align-top" aria-hidden="true"><use href="{{ site.baseurl }}/dist/svg/sprites.svg#it-instagram"></use></svg><span class="visually-hidden">Instagram (link esterno)</span></a>
              </li>
              <li class="list-inline-item">
                <a class="p-2 text-white" href="#"><svg class="icon icon-sm icon-inverse align-top" aria-hidden="true"><use href="{{ site.baseurl }}/dist/svg/sprites.svg#it-twitter"></use></svg><span class="visually-hidden">X (link esterno)</span></a>
              </li>
              <li class="list-inline-item">
                <a class="p-2 text-white" href="#"><svg class="icon icon-sm icon-inverse align-top" aria-hidden="true"><use href="{{ site.baseurl }}/dist/svg/sprites.svg#it-whatsapp"></use></svg><span class="visually-hidden">WhatsApp (link esterno)</span></a>
              </li>
              <li class="list-inline-item">
                <a class="p-2 text-white" href="#"><svg class="icon icon-sm icon-inverse align-top" aria-hidden="true"><use href="{{ site.baseurl }}/dist/svg/sprites.svg#it-linkedin"></use></svg><span class="visually-hidden">LinkedIn (link esterno)</span></a>
              </li>
            </ul>
            <div class="link-list-wrapper">
              <ul class="footer-list link-list clearfix">
                <li><a class="list-item" href="#">Social media policy</a></li>
                <li><a class="list-item fw-bold" href="#">Devolvi il 5x1000 al CNR</a></li>
              </ul>
            </div>
          </div>
        </div>
      </section>
    </div>
  </div>
  <div class="it-footer-small-prints clearfix">
    <div class="container">
      <ul class="it-footer-small-prints-list list-inline mb-0 d-flex flex-column flex-md-row">
        <li class="list-inline-item"><a href="#">Media Policy</a></li>
        <li class="list-inline-item"><a href="#">Note Legali</a></li>
        <li class="list-inline-item"><a href="#">Privacy Policy</a></li>
        <li class="list-inline-item"><a href="#">Mappa del sito</a></li>
        <li class="list-inline-item"><a href="https://form.agid.gov.it/view/xyz">Dichiarazione Accessibilità <span class="visually-hidden">(link esterno su sito AgID)</span></a></li>
      </ul>
    </div>
  </div>
</footer>
{% endcapture %}{% include example.html content=example %}

{% include properties.md properties=site.data.cprops.footer %}
## Breaking change

{% capture callout %}
- Per la `<section>` di branding dell'ente: aggiunta classe `.pb-4`.
- Per la `<section>` che ospita sitemap o link: aggiunta classe `.pt-2`. 
  - Per i `<div>` interni di questa seconda sezione è stato corretto il responsive: rimossa classe `.col-md-3` e aggiunta la classe `.pb-3`.
- Per la `<section>` che presenta dati dell'ente e contatti: cambiato da `.py-4` a `.pt-4`.
  - Per i `<div>` interni di questa terza sezione sono state corrette le spaziature verticali: cambiato da `.pb-2` a `.mt-2` 
- La classe che controlla il colore delle icone social ha cambiato nome: `.icon-white` diventa `.icon-inverse`.
- Aggiunto il markup per mostrare il campo input per l'iscrizione alla newsletter.
{% endcapture %}{% include callout.html content=callout version="3.0.0" type="danger" %}
