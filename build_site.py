#!/usr/bin/env python3
"""Builds Cutout's standalone 12-locale Help & Privacy site (Seamless Paper aesthetic)."""
from __future__ import annotations

import html
from pathlib import Path

ROOT = Path(__file__).resolve().parent
BASE_URL = "https://hayriodabas.github.io/cutout-help"
CONTACT_EMAIL = "hayriodabas@gmail.com"
UPDATED = "2026-11-25"
BUNDLE_ID = "app.klarwerk.cutout"
IAP_ID = "app.klarwerk.cutout.unlock"

CSS = """\
:root {
  color-scheme: light dark;
  --paper: #efede8;
  --surface: #f8f7f4;
  --checker-a: #e6e3dc;
  --checker-b: #f4f2ed;
  --ink: #17181a;
  --ink2: #4c4e54;
  --hairline: rgba(23, 24, 26, 0.12);
  --signal: #bd3b1f;
  --signal-text: #a13017;
  --signal-soft: rgba(189, 59, 31, 0.09);
}
@media (prefers-color-scheme: dark) {
  :root {
    --paper: #121315;
    --surface: #1b1c1f;
    --checker-a: #2a2b2f;
    --checker-b: #222326;
    --ink: #eceae5;
    --ink2: #a9abb1;
    --hairline: rgba(236, 234, 229, 0.14);
    --signal: #ff6b4d;
    --signal-text: #ff8269;
    --signal-soft: rgba(255, 107, 77, 0.14);
  }
}
* { box-sizing: border-box; }
body {
  margin: 0;
  background: var(--paper);
  color: var(--ink);
  font: 16.5px/1.62 -apple-system, BlinkMacSystemFont, "SF Pro Text", "Segoe UI", Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
}
.sweep-rule {
  position: relative;
  height: 22px;
  border-bottom: 1px solid var(--hairline);
  background: linear-gradient(90deg, #f8f7f4 0 38%, #dcdad4 38% 50%, #e4d9c8 50% 62%, #d4ddd3 62% 74%, #d3dce6 74% 86%, #2a2c30 86% 100%);
}
.sweep-rule::after {
  content: "";
  position: absolute;
  left: 50%;
  top: 0;
  width: 3px;
  height: 22px;
  transform: translateX(-50%);
  background: var(--signal);
}
main {
  max-width: 760px;
  margin: 0 auto;
  padding: 36px 20px 68px;
}
header.masthead {
  display: flex;
  gap: 16px;
  align-items: center;
  margin-bottom: 14px;
}
header.masthead img {
  width: 60px;
  height: 60px;
  border-radius: 14px;
  border: 1px solid var(--hairline);
  flex-shrink: 0;
}
.kicker {
  font-size: 12px;
  font-weight: 700;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--signal-text);
}
h1 {
  font-size: 36px;
  line-height: 1.1;
  font-weight: 750;
  margin: 4px 0 0;
  letter-spacing: -0.02em;
}
.lede {
  font-size: 18px;
  color: var(--ink2);
  margin: 8px 0 22px;
}
nav.top-nav {
  display: flex;
  flex-wrap: wrap;
  gap: 10px 18px;
  padding: 12px 0;
  border-top: 1px solid var(--hairline);
  border-bottom: 1px solid var(--hairline);
  margin-bottom: 16px;
  font-size: 14.5px;
  font-weight: 600;
}
.lang-bar {
  display: flex;
  flex-wrap: wrap;
  gap: 7px;
  margin: 0 0 28px;
}
.lang-pill {
  font-size: 12.5px;
  padding: 4px 10px;
  border-radius: 999px;
  border: 1px solid var(--hairline);
  background: var(--surface);
  color: var(--ink2);
  text-decoration: none;
}
.lang-pill.active {
  background: var(--signal-soft);
  border-color: var(--signal);
  color: var(--signal-text);
  font-weight: 600;
}
a {
  color: var(--signal-text);
  text-decoration-thickness: 1.5px;
  text-underline-offset: 3px;
}
h2 {
  font-size: 21px;
  line-height: 1.25;
  margin: 32px 0 10px;
  font-weight: 680;
}
.panel {
  background: var(--surface);
  border: 1px solid var(--hairline);
  border-radius: 10px;
  padding: 16px 18px;
  margin: 12px 0;
}
.panel strong {
  display: block;
  margin-bottom: 4px;
}
ul, ol {
  padding-left: 20px;
}
li {
  margin: 7px 0;
}
table {
  width: 100%;
  border-collapse: collapse;
  margin: 14px 0;
  background: var(--surface);
  border: 1px solid var(--hairline);
  border-radius: 10px;
  overflow: hidden;
}
th, td {
  text-align: left;
  padding: 11px 14px;
  border-bottom: 1px solid var(--hairline);
  font-size: 15px;
  vertical-align: top;
}
th {
  width: 32%;
  font-size: 12px;
  text-transform: uppercase;
  letter-spacing: 0.08em;
  color: var(--ink2);
}
tr:last-child th, tr:last-child td { border-bottom: none; }
.swatches {
  display: flex;
  flex-wrap: wrap;
  gap: 8px;
  margin: 16px 0 8px;
}
.swatch {
  display: inline-flex;
  align-items: center;
  gap: 7px;
  padding: 5px 10px;
  border-radius: 999px;
  background: var(--surface);
  border: 1px solid var(--hairline);
  font-size: 12.5px;
  color: var(--ink2);
}
.swatch i {
  width: 12px;
  height: 12px;
  border-radius: 50%;
  border: 1px solid var(--hairline);
  display: inline-block;
}
.cards {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(240px, 1fr));
  gap: 12px;
  margin: 18px 0;
}
.card {
  display: block;
  text-decoration: none;
  background: var(--surface);
  border: 1px solid var(--hairline);
  border-radius: 10px;
  padding: 18px;
  color: var(--ink);
}
.card:hover { border-color: var(--signal); }
.card strong {
  display: block;
  font-size: 17px;
  color: var(--signal-text);
  margin-bottom: 6px;
}
.card span {
  font-size: 14.5px;
  color: var(--ink2);
}
footer {
  margin-top: 44px;
  padding-top: 16px;
  border-top: 1px solid var(--hairline);
  color: var(--ink2);
  font-size: 13.5px;
}
@media (max-width: 560px) {
  h1 { font-size: 28px; }
  main { padding: 24px 16px 52px; }
  th { width: 38%; }
}
"""

LOCALES: dict[str, dict] = {
    "en-US": {
        "name": "English",
        "html_lang": "en",
        "app": "Cutout",
        "full_name": "Cutout: Product Photo Backdrop",
        "nav_home": "Overview",
        "nav_help": "Help",
        "nav_privacy": "Privacy Policy",
        "papers": [("Studio White", "#f8f7f4"), ("Paper Grey", "#dcdad4"), ("Sand", "#e4d9c8"), ("Sage", "#d4ddd3"), ("Mist", "#d3dce6"), ("Charcoal", "#2a2c30")],
        "contact_title": "Contact & Support",
        "contact_body": f"Questions, bug reports, or privacy requests for Cutout: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>.",
        "updated": f"Updated {UPDATED} · {BUNDLE_ID} · Hayri Odabaş",
        "hub": {
            "lede": "On-device product cutout and seamless paper studio backdrop with silhouette-drawn shadows.",
            "help_desc": "Guides for Standing & Laid Flat lighting, Clean Edge, manual brush refinement, Batch mode, and Cutout Pro.",
            "privacy_desc": "On-device Vision processing, no uploads, no accounts, no analytics or tracking SDKs.",
        },
        "help": {
            "title": "Help & Studio Guide",
            "lede": "Place product photos on a curved seamless paper roll or clean white square — all processed on your device.",
            "steps_title": "Workflow guide",
            "steps": [
                ("Pick a photo or start with a sample", "Tap Choose Photo to import from your library, or open either home sample (the mug or the knit sweater) to explore lighting, shadows, and edge tools without changing any of your own photos."),
                ("Standing vs. Laid flat & Lamp direction", "Open Light. Standing places the subject on the curved paper floor with a contact shadow whose darkness follows the object's silhouette (dense under a mug body, lighter under the handle). Laid flat centers flat-lay items like knitwear or shirts on the paper with a directional side shadow. Drag across the preview or move the Lamp slider to flip shadow direction — free on every photo."),
                ("Clean Edge & manual brush", "Clean Edge tightens soft masks and removes background color spill (for example a green sofa tint along a white edge). In Refine, toggle Clean Edge off to inspect the raw mask, use the Erase or Restore brush with the overhead magnifier, and undo step by step."),
                ("Looks, Export preview & Batch", "Studio, Listing, Transparent PNG, and Catalog (Pro) apply frame ratio, paper tone, and padding in one tap. Free exports save up to 1600 px with no watermark. Cutout Pro (one-time purchase) adds full-resolution export, five more paper rolls, solid colors with custom tint and flat-backdrop shadow, 4:5 / 3:4 / 16:9 ratios, multiple-subject selection, softer edges, and Batch runs of up to 30 photos (tap any finished batch item to fix its cutout before saving)."),
            ],
            "faq_title": "Frequently asked questions",
            "faq": [
                ("Are my product photos uploaded to a server?", "No. Foreground segmentation runs locally on your iPhone or iPad via Apple's Vision framework. Original photos and edited projects stay strictly on your device."),
                ("How do I erase all saved projects?", "Open Settings › Delete All Saved Edits inside Cutout to remove every locally stored edit, or remove individual items from Recent on the home screen."),
                ("Why does Cutout ask for permission when saving?", "Choosing photos uses Apple's privacy-preserving PHPicker without full library access. Writing finished pictures back uses Photos add-only authorization only when you tap Save."),
                ("How do I restore Cutout Pro?", f"Cutout Pro ({IAP_ID}) is a single non-consumable unlock. On the same Apple Account, open Settings › Restore Purchase inside the app. Store refunds are handled by Apple at reportaproblem.apple.com."),
            ],
        },
        "privacy": {
            "title": "Privacy Policy",
            "lede": "Cutout processes every image on your device, collects no personal data, and never uploads your photos.",
            "summary_title": "At a glance",
            "rows": [
                ("Photo processing", "On-device via Apple Vision (VNGenerateForegroundInstanceMaskRequest). Images never leave your device."),
                ("Photo Library access", "Importing uses the system photo picker; saving requests Photos add-only access only when you choose Save."),
                ("Saved edits & settings", "Stored locally inside Cutout's app container (Application Support and UserDefaults). No cloud sync or account."),
                ("Analytics & third-party SDKs", "None. Zero crash reporters, ad networks, or tracking frameworks."),
                ("Payments", f"Processed solely by Apple StoreKit for the optional one-time Cutout Pro unlock ({IAP_ID})."),
            ],
            "sections": [
                ("Data Not Collected", "Hayri Odabaş does not collect, store, sell, or share any personal information, identifiers, usage metrics, diagnostics, or images from Cutout."),
                ("Your Control & Deletion", "Open Settings › Delete All Saved Edits to wipe stored projects and masks at any time, or uninstall Cutout to remove all app container files."),
                ("Third-Party Services", "No third-party cloud APIs are contacted during editing. StoreKit communicates with Apple only when viewing price, buying, or restoring Cutout Pro."),
                ("Children & Contact", f"Cutout does not knowingly collect data from anyone, including children. Reach the developer anytime at {CONTACT_EMAIL}."),
            ],
        },
    },
    "de-DE": {
        "name": "Deutsch",
        "html_lang": "de",
        "app": "Hintergrund Weg",
        "full_name": "Hintergrund Weg: Freistellen",
        "nav_home": "Übersicht",
        "nav_help": "Hilfe",
        "nav_privacy": "Datenschutz",
        "papers": [("Studioweiß", "#f8f7f4"), ("Papiergrau", "#dcdad4"), ("Sand", "#e4d9c8"), ("Salbei", "#d4ddd3"), ("Nebel", "#d3dce6"), ("Anthrazit", "#2a2c30")],
        "contact_title": "Kontakt & Support",
        "contact_body": f"Fragen oder Hinweise zu Hintergrund Weg: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>.",
        "updated": f"Stand {UPDATED} · {BUNDLE_ID} · Hayri Odabaş",
        "hub": {
            "lede": "Produktfotos auf dem Gerät freistellen und mit formgenauem Schatten auf Studio-Hohlkehle setzen.",
            "help_desc": "Anleitung für Stehend & Liegend, Lampenrichtung, Saubere Kante, Pinsel, Stapelverarbeitung und Pro.",
            "privacy_desc": "Lokale Vision-Erkennung auf dem Gerät, kein Upload, kein Konto, keine Tracking-SDKs.",
        },
        "help": {
            "title": "Hilfe & Anleitung",
            "lede": "Produkte direkt auf iPhone oder iPad freistellen und auf eine nahtlose Studio-Hohlkehle setzen.",
            "steps_title": "So funktioniert's",
            "steps": [
                ("Foto wählen oder Beispiel testen", "Tippe auf Foto wählen oder probiere Tasse und Pullover direkt auf dem Startbildschirm aus."),
                ("Stehend, Liegend & Lampe", "Unter Licht wählst du zwischen Stehend (auf der Bodenlinie) und Liegend (Draufsicht/Flachlage). Ziehe über das Bild oder nutze den Lampenregler, um die Schattenrichtung kostenlos zu drehen."),
                ("Saubere Kante & Pinsel", "Saubere Kante entfernt Farbsäume des alten Hintergrunds. Unter Verfeinern kannst du sie prüfen oder mit Radierer, Wiederherstellen-Pinsel, Lupe und Widerrufen manuell nacharbeiten."),
                ("Looks, Export & Stapel", "Studio, Inserat, Transparentes PNG und Katalog (Pro) setzen Format und Papier in einem Tipp. Kostenlos bis 1600 px ohne Wasserzeichen; Pro (Einmalkauf) bringt volle Auflösung, 5 weitere Papiertöne, Volltonfarben + Schatten, Formate 4:5/3:4/16:9, Motivauswahl und Stapel bis 30 Fotos."),
            ],
            "faq_title": "Häufige Fragen",
            "faq": [
                ("Werden meine Fotos hochgeladen?", "Nein. Die Freistellung läuft vollständig lokal über Apples Vision-Framework auf deinem Gerät."),
                ("Wie lösche ich gespeicherte Bearbeitungen?", "Unter Einstellungen › Alle gespeicherten Bearbeitungen löschen entfernst du lokale Projekte restlos."),
                ("Welche Fotorechte braucht die App?", "Die Auswahl nutzt Apples System-Auswahl ohne Vollzugriff; zum Sichern in Fotos wird nur Schreibzugriff angefragt."),
                ("Kauf wiederherstellen", "Tippe mit derselben Apple-ID in den Einstellungen auf Kauf wiederherstellen. Rückerstattungen erfolgen über reportaproblem.apple.com."),
            ],
        },
        "privacy": {
            "title": "Datenschutzerklärung",
            "lede": "Hintergrund Weg verarbeitet alle Bilder ausschließlich lokal und erhebt keinerlei personenbezogene Daten.",
            "summary_title": "Kurzfassung",
            "rows": [
                ("Bildverarbeitung", "Ausschließlich lokal auf dem Gerät via Apple Vision. Keine Uploads."),
                ("Fotozugriff", "Import über den System-Fotowähler; beim Sichern nur Hinzufügen-Berechtigung."),
                ("Lokaler Speicher", "Projekte und Einstellungen verbleiben im App-Container auf deinem Gerät."),
                ("Analyse & Werbung", "Keine Drittanbieter-SDKs, kein Tracking, keine Konten."),
                ("In-App-Kauf", f"Einmalkauf Hintergrund Weg Pro ({IAP_ID}) über Apple StoreKit."),
            ],
            "sections": [
                ("Keine Datenerfassung", "Wir erheben, speichern, verkaufen oder teilen weder Bilder noch Nutzungsdaten oder Geräte-IDs."),
                ("Löschen", "In den App-Einstellungen lassen sich alle gespeicherten Projekte löschen; die Deinstallation entfernt alle lokalen Dateien."),
                ("Kontakt", f"Anfragen zum Datenschutz bitte an {CONTACT_EMAIL}."),
            ],
        },
    },
    "es-ES": {
        "name": "Español",
        "html_lang": "es",
        "app": "Quitar Fondo",
        "full_name": "Quitar Fondo: Fotos Producto",
        "nav_home": "Resumen",
        "nav_help": "Ayuda",
        "nav_privacy": "Privacidad",
        "papers": [("Blanco estudio", "#f8f7f4"), ("Gris papel", "#dcdad4"), ("Arena", "#e4d9c8"), ("Salvia", "#d4ddd3"), ("Niebla", "#d3dce6"), ("Carbón", "#2a2c30")],
        "contact_title": "Contacto y soporte",
        "contact_body": f"Consultas o fallos en Quitar Fondo: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>.",
        "updated": f"Actualizado {UPDATED} · {BUNDLE_ID} · Hayri Odabaş",
        "hub": {
            "lede": "Recorte de producto en el dispositivo sobre papel infinito de estudio y sombra natural del contorno.",
            "help_desc": "Guía de De pie y Extendido, lámpara, Borde limpio, pincel, lotes y versión Pro.",
            "privacy_desc": "Procesamiento local con Apple Vision, sin subidas, sin cuenta ni rastreadores.",
        },
        "help": {
            "title": "Ayuda y guía",
            "lede": "Prepara fotos de producto sobre fondo infinito en tu iPhone o iPad sin subir ningún archivo.",
            "steps_title": "Cómo usarla",
            "steps": [
                ("Elige una foto o prueba un ejemplo", "Pulsa Elegir foto o prueba primero la taza y el jersey de la pantalla inicial."),
                ("De pie o Extendido y lámpara", "En Luz escoge De pie (sobre la línea del suelo) o Extendido (vista cenital/colgada). Arrastra sobre la imagen o desliza la lámpara para cambiar el lado de la sombra gratis."),
                ("Borde limpio y pincel manual", "Borde limpio elimina halos del color anterior. En Retocar puedes desactivarlo o corregir a mano con borrador, restaurar y lupa."),
                ("Aspectos, exportación y lotes", "Estudio, Anuncio, PNG transparente y Catálogo (Pro) aplican encuadre y papel al instante. Gratis hasta 1600 px sin marca de agua; Pro (pago único) añade tamaño completo, 5 papeles extra, colores lisos con sombra, 4:5/3:4/16:9, selección de varios sujetos y lotes de hasta 30 fotos."),
            ],
            "faq_title": "Preguntas frecuentes",
            "faq": [
                ("¿Se suben mis fotos a internet?", "No. La detección del sujeto ocurre íntegramente en el dispositivo mediante Apple Vision."),
                ("¿Cómo borro los proyectos guardados?", "En Ajustes › Eliminar todas las ediciones guardadas borras todos los recortes locales."),
                ("¿Cómo restauro Quitar Fondo Pro?", "Usa Restaurar compra en Ajustes con la misma Cuenta de Apple. Reembolsos en reportaproblem.apple.com."),
            ],
        },
        "privacy": {
            "title": "Política de privacidad",
            "lede": "Quitar Fondo procesa cada fotografía en el dispositivo y no recopila datos personales.",
            "summary_title": "Resumen",
            "rows": [
                ("Procesamiento", "Local con Apple Vision. Ninguna imagen sale del dispositivo."),
                ("Fotos", "Importación mediante el selector del sistema; al guardar, solo permiso de añadir."),
                ("Almacenamiento", "Proyectos y ajustes locales en el dispositivo. Sin cuentas ni nube."),
                ("SDKs de análisis", "Ninguno. Sin publicidad ni telemetría."),
                ("Pagos", f"Compra única Quitar Fondo Pro ({IAP_ID}) gestionada por Apple StoreKit."),
            ],
            "sections": [
                ("Sin recopilación de datos", "No recopilamos, compartimos ni vendemos imágenes, identificadores ni datos de uso."),
                ("Eliminación", "Puedes borrar las ediciones guardadas desde Ajustes o eliminar la app en cualquier momento."),
                ("Contacto", f"Para cualquier cuestión de privacidad escribe a {CONTACT_EMAIL}."),
            ],
        },
    },
    "fr-FR": {
        "name": "Français",
        "html_lang": "fr",
        "app": "Supprimer Fond",
        "full_name": "Supprimer Fond: Détourage",
        "nav_home": "Aperçu",
        "nav_help": "Aide",
        "nav_privacy": "Confidentialité",
        "papers": [("Blanc studio", "#f8f7f4"), ("Gris papier", "#dcdad4"), ("Sable", "#e4d9c8"), ("Sauge", "#d4ddd3"), ("Brume", "#d3dce6"), ("Anthracite", "#2a2c30")],
        "contact_title": "Contact et assistance",
        "contact_body": f"Questions ou retours sur Supprimer Fond : <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>.",
        "updated": f"Mis à jour le {UPDATED} · {BUNDLE_ID} · Hayri Odabaş",
        "hub": {
            "lede": "Détourage produit sur l'appareil et papier studio sans couture avec ombre tirée de la silhouette.",
            "help_desc": "Guide Debout & À plat, lampe, Bord net, pinceau, lots et Supprimer Fond Pro.",
            "privacy_desc": "Traitement local Apple Vision, aucun envoi de photo, aucun compte ni pistage.",
        },
        "help": {
            "title": "Aide et guide",
            "lede": "Posez vos photos produit sur un fond studio propre, entièrement calculé sur iPhone ou iPad.",
            "steps_title": "Mode d'emploi",
            "steps": [
                ("Choisir une photo ou un exemple", "Touchez Choisir une photo ou testez d'abord la tasse et le pull présents sur l'écran d'accueil."),
                ("Debout, À plat & Lampe", "Dans Lumière, choisissez Debout (posé au sol) ou À plat (vêtement/vue du dessus). Faites glisser sur l'image ou déplacez le curseur de lampe pour orienter l'ombre gratuitement."),
                ("Bord net et pinceau", "Bord net supprime les franges colorées de l'ancien arrière-plan. Dans Retoucher, affinez au pinceau avec la loupe et l'annulation illimitée."),
                ("Styles, export et lots", "Studio, Annonce, PNG transparent et Catalogue (Pro). Export gratuit jusqu'à 1600 px sans filigrane ; Pro (achat unique) ajoute la pleine définition, 5 tons de papier, couleurs unies avec ombre, ratios 4:5/3:4/16:9, choix multi-sujets et lots jusqu'à 30 photos."),
            ],
            "faq_title": "Questions fréquentes",
            "faq": [
                ("Mes photos quittent-elles l'appareil ?", "Non. La segmentation tourne localement via Apple Vision sans connexion serveur."),
                ("Comment tout effacer ?", "Ouvrez Réglages › Supprimer toutes les retouches enregistrées dans l'app."),
                ("Restaurer l'achat Pro", "Dans Réglages › Restaurer l'achat avec le même compte Apple. Remboursements via reportaproblem.apple.com."),
            ],
        },
        "privacy": {
            "title": "Politique de confidentialité",
            "lede": "Supprimer Fond traite vos images localement, ne demande aucun compte et ne collecte aucune donnée.",
            "summary_title": "En bref",
            "rows": [
                ("Traitement d'image", "100 % local sur l'appareil avec Apple Vision."),
                ("Photothèque", "Sélecteur système pour importer ; ajout seul lors de l'enregistrement."),
                ("Stockage local", "Retouches conservées sur l'appareil uniquement."),
                ("Analyse et pub", "Aucun SDK tiers, aucune statistique, aucune publicité."),
                ("Paiement", f"Achat unique Supprimer Fond Pro ({IAP_ID}) via Apple StoreKit."),
            ],
            "sections": [
                ("Aucune donnée collectée", "Aucune donnée personnelle, identifiant ou image n'est collecté, vendu ou transmis."),
                ("Contrôle", "Supprimez vos projets dans les réglages de l'application ou en la désinstallant."),
                ("Contact", f"Écrivez à {CONTACT_EMAIL} pour toute question."),
            ],
        },
    },
    "it": {
        "name": "Italiano",
        "html_lang": "it",
        "app": "Rimuovi Sfondo",
        "full_name": "Rimuovi Sfondo: Foto Prodotti",
        "nav_home": "Panoramica",
        "nav_help": "Aiuto",
        "nav_privacy": "Privacy",
        "papers": [("Bianco studio", "#f8f7f4"), ("Grigio carta", "#dcdad4"), ("Sabbia", "#e4d9c8"), ("Salvia", "#d4ddd3"), ("Nebbia", "#d3dce6"), ("Antracite", "#2a2c30")],
        "contact_title": "Contatti e supporto",
        "contact_body": f"Domande o segnalazioni su Rimuovi Sfondo: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>.",
        "updated": f"Aggiornato {UPDATED} · {BUNDLE_ID} · Hayri Odabaş",
        "hub": {
            "lede": "Scontorno prodotti su dispositivo e fondale di carta da studio con ombra dal contorno reale.",
            "help_desc": "Guida per In piedi e Disteso, lampada, Bordo pulito, pennello, serie e Pro.",
            "privacy_desc": "Elaborazione locale con Apple Vision, nessun caricamento, nessun account né tracciamento.",
        },
        "help": {
            "title": "Guida e supporto",
            "lede": "Appoggia le foto dei prodotti su un fondale da studio senza giunte, tutto su iPhone o iPad.",
            "steps_title": "Come funziona",
            "steps": [
                ("Scegli una foto o un esempio", "Tocca Scegli foto oppure prova subito la tazza e il maglione dalla schermata iniziale."),
                ("In piedi, Disteso & Lampada", "In Luce scegli In piedi (sulla linea del piano) o Disteso. Trascina sull'immagine o regola la lampada per spostare l'ombra gratis."),
                ("Bordo pulito e pennello", "Bordo pulito rimuove aloni di colore del vecchio sfondo. In Rifinisci puoi intervenire a mano con pennello, lente e annulla."),
                ("Look, esportazione e serie", "Studio, Annuncio, PNG trasparente e Catalogo (Pro). Gratis fino a 1600 px senza filigrana; Pro (acquisto unico) sblocca piena risoluzione, 5 toni di carta, tinte unite con ombra, 4:5/3:4/16:9, soggetti multipli e serie fino a 30 foto."),
            ],
            "faq_title": "Domande frequenti",
            "faq": [
                ("Le foto vengono inviate a un server?", "No. Il rilevamento avviene interamente sul dispositivo tramite Apple Vision."),
                ("Come cancello le modifiche salvate?", "Apri Impostazioni › Elimina tutte le modifiche salvate."),
                ("Ripristinare Rimuovi Sfondo Pro", "Usa Ripristina acquisto nelle Impostazioni con lo stesso Account Apple (rimborsi su reportaproblem.apple.com)."),
            ],
        },
        "privacy": {
            "title": "Informativa sulla privacy",
            "lede": "Rimuovi Sfondo elabora tutto sul dispositivo e non raccoglie alcun dato personale.",
            "summary_title": "In sintesi",
            "rows": [
                ("Elaborazione", "Solo locale sul dispositivo tramite Apple Vision."),
                ("Libreria Foto", "Selettore di sistema per importare; solo aggiunta al salvataggio."),
                ("Archivio locale", "Modifiche e preferenze restano sul dispositivo."),
                ("Tracciamento", "Nessun SDK di analisi o pubblicità, nessun account."),
                ("Acquisti", f"Acquisto singolo Rimuovi Sfondo Pro ({IAP_ID}) gestito da Apple StoreKit."),
            ],
            "sections": [
                ("Nessuna raccolta dati", "Non raccogliamo, trasmettiamo né vendiamo foto o dati personali."),
                ("Eliminazione", "Cancella le modifiche salvate dalle Impostazioni o rimuovi l'app."),
                ("Contatti", f"Scrivi a {CONTACT_EMAIL} per richieste sulla privacy."),
            ],
        },
    },
    "ja": {
        "name": "日本語",
        "html_lang": "ja",
        "app": "背景削除",
        "full_name": "背景削除: 切り抜き写真",
        "nav_home": "概要",
        "nav_help": "ヘルプ",
        "nav_privacy": "プライバシー",
        "papers": [("スタジオホワイト", "#f8f7f4"), ("ペーパーグレー", "#dcdad4"), ("サンド", "#e4d9c8"), ("セージ", "#d4ddd3"), ("ミスト", "#d3dce6"), ("チャコール", "#2a2c30")],
        "contact_title": "お問い合わせ",
        "contact_body": f"背景削除に関するご質問や不具合のご報告：<a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>",
        "updated": f"更新日 {UPDATED} · {BUNDLE_ID} · Hayri Odabaş",
        "hub": {
            "lede": "端末内処理で商品を切り抜き、輪郭から生まれる自然な影つきのスタジオ背景紙に配置。",
            "help_desc": "立てる・平置き・ライト調整・きれいな縁・ブラシ・一括処理と Pro のご案内。",
            "privacy_desc": "Apple Vision による完全端末内処理。アップロード、アカウント、追跡 SDK なし。",
        },
        "help": {
            "title": "ヘルプ・使い方",
            "lede": "商品写真を iPhone や iPad の中だけで切り抜き、継ぎ目のないスタジオ背景紙に仕上げます。",
            "steps_title": "基本の流れ",
            "steps": [
                ("写真を選ぶ・サンプルで試す", "「写真を選ぶ」で読み込むか、ホーム画面のマグカップ・セーターで機能を試せます。"),
                ("立てる / 平置き・ライト", "「ライト」で置き方を選びます。画像上をドラッグするかスライダーを動かすと影の向きが変わり、すべて無料です。"),
                ("きれいな縁と手動ブラシ", "元の背景色の写り込みを除去します。「修正」でスイッチのオン/オフや拡大鏡つきブラシ修正ができます。"),
                ("スタイル・書き出し・一括処理", "スタジオ・出品用・透明PNG・カタログ（Pro）を選択。無料は長辺 1600 px まで透かしなし。Pro（買い切り）でフル解像度、5色の紙、単色背景と影、4:5/3:4/16:9、複数被写体選択、最大30枚一括処理に対応。"),
            ],
            "faq_title": "よくある質問",
            "faq": [
                ("写真はサーバーに送られますか？", "いいえ。Apple Vision を用いて端末内だけで処理されます。"),
                ("保存した編集を削除するには？", "アプリ内の「設定 › 保存済みの編集をすべて削除」で一括消去できます。"),
                ("Pro 購入の復元方法", "同じ Apple Account で「設定 › 購入を復元」をタップしてください。返金は reportaproblem.apple.com で手続きできます。"),
            ],
        },
        "privacy": {
            "title": "プライバシーポリシー",
            "lede": "「背景削除」はすべての画像処理を端末内で完結し、個人情報を一切収集しません。",
            "summary_title": "概要",
            "rows": [
                ("画像処理", "Apple Vision により端末内のみで完結。外部送信なし。"),
                ("写真アクセス", "読み込みはシステムピッカーを使用、保存時のみ追加権限を使用。"),
                ("データ保存", "編集履歴と設定は端末内のアプリ領域にのみ保存。"),
                ("解析・広告", "第三者製解析 SDK・広告・アカウントなし。"),
                ("課金", f"買い切り版（{IAP_ID}）のみ Apple StoreKit を利用。"),
            ],
            "sections": [
                ("情報収集なし", "開発者は写真、識別子、利用状況などのデータを収集・保存・提供しません。"),
                ("データの削除", "アプリ内設定から保存済み編集を削除するか、アプリを削除することで消去できます。"),
                ("連絡先", f"お問い合わせは {CONTACT_EMAIL} までご連絡ください。"),
            ],
        },
    },
    "ko": {
        "name": "한국어",
        "html_lang": "ko",
        "app": "배경 제거",
        "full_name": "배경 제거: 누끼 따기",
        "nav_home": "개요",
        "nav_help": "도움말",
        "nav_privacy": "개인정보 처리방침",
        "papers": [("스튜디오 화이트", "#f8f7f4"), ("페이퍼 그레이", "#dcdad4"), ("샌드", "#e4d9c8"), ("세이지", "#d4ddd3"), ("미스트", "#d3dce6"), ("차콜", "#2a2c30")],
        "contact_title": "문의 및 지원",
        "contact_body": f"배경 제거 앱 문의 및 오류 제보: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>",
        "updated": f"업데이트 {UPDATED} · {BUNDLE_ID} · Hayri Odabaş",
        "hub": {
            "lede": "기기 안에서 상품 배경을 지우고 피사체 모양의 그림자가 담긴 스튜디오 종이 배경에 배치합니다.",
            "help_desc": "세워서/펼쳐서, 조명 이동, 깔끔한 가장자리, 브러시 다듬기, 일괄 처리 및 Pro 안내.",
            "privacy_desc": "Apple Vision 기기 내 처리. 사진 업로드, 계정, 추적 SDK 없음.",
        },
        "help": {
            "title": "도움말 및 사용 안내",
            "lede": "업로드 없이 iPhone과 iPad 안에서 상품 사진을 깔끔한 스튜디오 배경으로 바꿉니다.",
            "steps_title": "사용 순서",
            "steps": [
                ("사진 고르기 또는 샘플 체험", "홈 화면에서 사진 선택을 누르거나 머그잔·스웨터 샘플로 먼저 기능을 시험해 보세요."),
                ("세워서 / 펼쳐서 및 조명", "조명에서 배치를 고르고 사진 위를 드래그해 그림자 방향을 무료로 조절하세요."),
                ("깔끔한 가장자리 및 브러시", "원래 배경색 번짐을 제거하며, 다듬기에서 확대경이 달린 브러시로 세밀하게 수정할 수 있습니다."),
                ("프리셋, 내보내기, 일괄 처리", "무료는 긴 변 1600px까지 워터마크 없이 저장합니다. Pro(1회 구입)는 원본 해상도, 종이 5종, 단색+그림자, 4:5/3:4/16:9 비율, 다중 피사체 선택, 최대 30장 일괄 처리를 제공합니다."),
            ],
            "faq_title": "자주 묻는 질문",
            "faq": [
                ("사진이 서버로 전송되나요?", "아니요. Apple Vision을 통해 기기 내부에서만 처리됩니다."),
                ("저장된 편집을 모두 지우려면?", "설정 › 저장된 모든 편집 삭제를 누르면 기기 내 프로젝트가 삭제됩니다."),
                ("구입 복원", "같은 Apple 계정으로 설정 › 구입 복원을 누르세요. 환불은 reportaproblem.apple.com에서 진행됩니다."),
            ],
        },
        "privacy": {
            "title": "개인정보 처리방침",
            "lede": "배경 제거는 모든 이미지를 기기에서 처리하며 개인정보를 수집하지 않습니다.",
            "summary_title": "요약",
            "rows": [
                ("이미지 처리", "Apple Vision 기반 완전 온디바이스 처리. 외부 전송 없음."),
                ("사진 접근", "불러오기는 시스템 사진 선택기, 저장 시에만 추가 권한 요청."),
                ("로컬 저장", "편집 기록과 설정은 앱 내부 저장소에만 보관."),
                ("분석 및 광고", "제3자 추적 SDK, 광고, 로그인 없음."),
                ("결제", f"Apple StoreKit을 통한 1회성 Pro 잠금 해제 ({IAP_ID})."),
            ],
            "sections": [
                ("수집하는 정보 없음", "어떠한 사진, 식별자, 사용 통계도 수집·저장·공유하지 않습니다."),
                ("삭제 및 제어", "설정에서 모든 저장된 편집을 삭제하거나 앱을 삭제하여 데이터를 지울 수 있습니다."),
                ("연락처", f"개인정보 관련 문의는 {CONTACT_EMAIL}로 보내 주세요."),
            ],
        },
    },
    "nl-NL": {
        "name": "Nederlands",
        "html_lang": "nl",
        "app": "Achtergrond Weg",
        "full_name": "Achtergrond Weg: Productfoto",
        "nav_home": "Overzicht",
        "nav_help": "Hulp",
        "nav_privacy": "Privacy",
        "papers": [("Studiowit", "#f8f7f4"), ("Papiergrijs", "#dcdad4"), ("Zand", "#e4d9c8"), ("Salie", "#d4ddd3"), ("Nevel", "#d3dce6"), ("Antraciet", "#2a2c30")],
        "contact_title": "Contact & ondersteuning",
        "contact_body": f"Vragen of opmerkingen over Achtergrond Weg: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>.",
        "updated": f"Bijgewerkt {UPDATED} · {BUNDLE_ID} · Hayri Odabaş",
        "hub": {
            "lede": "Productfoto's vrijstellen op je toestel en op een naadloos studiofond zetten met echte silhouetschaduw.",
            "help_desc": "Uitleg over Staand & Liggend, lamp, Schone rand, penseel, batches en Pro.",
            "privacy_desc": "Lokale verwerking met Apple Vision, geen uploads, geen account en geen trackers.",
        },
        "help": {
            "title": "Hulp & handleiding",
            "lede": "Zet producten rechtstreeks op je iPhone of iPad op een strak studiofond zonder foto's te uploaden.",
            "steps_title": "In vier stappen",
            "steps": [
                ("Foto kiezen of voorbeeld testen", "Tik op Kies foto of probeer direct de mok en trui op het beginscherm."),
                ("Staand, Liggend & Lamp", "Kies bij Licht voor Staand of Liggend en sleep over de foto om gratis de schaduwkant te verplaatsen."),
                ("Schone rand & penseel", "Schone rand verwijdert kleurzweem van de oude achtergrond; onder Verfijn werk je bij met penseel en vergrootglas."),
                ("Looks, export en batches", "Gratis export gaat tot 1600 px zonder watermerk. Pro (eenmalig) voegt volledige resolutie, 5 extra papiertinten, effen kleuren + schaduw, 4:5/3:4/16:9, onderwerpkeuze en batches tot 30 foto's toe."),
            ],
            "faq_title": "Veelgestelde vragen",
            "faq": [
                ("Worden mijn foto's geüpload?", "Nee. Alles draait lokaal via Apple Vision op je toestel."),
                ("Opgeslagen bewerkingen wissen", "Open Instellingen › Alle bewaarde bewerkingen verwijderen."),
                ("Aankoop herstellen", "Tik in Instellingen op Aankoop herstellen met dezelfde Apple Account (terugbetaling via reportaproblem.apple.com)."),
            ],
        },
        "privacy": {
            "title": "Privacybeleid",
            "lede": "Achtergrond Weg verwerkt alle beelden op het toestel en verzamelt geen persoonsgegevens.",
            "summary_title": "Kort overzicht",
            "rows": [
                ("Beeldverwerking", "Lokaal op het toestel via Apple Vision. Geen serveruploads."),
                ("Fototoegang", "Systeem-fotokiezer bij openen; alleen toevoegrechten bij bewaren."),
                ("Opslag", "Projecten en instellingen blijven lokaal in de app-container."),
                ("Tracking", "Geen analyse-SDK's, geen reclame, geen account."),
                ("Aankoop", f"Eenmalige ontgrendeling ({IAP_ID}) via Apple StoreKit."),
            ],
            "sections": [
                ("Geen gegevensverzameling", "Wij verzamelen, delen of verkopen geen foto's, id's of gebruiksstatistieken."),
                ("Verwijderen", "Verwijder opgeslagen bewerkingen via Instellingen of verwijder de app."),
                ("Contact", f"Mail voor privacyvragen naar {CONTACT_EMAIL}."),
            ],
        },
    },
    "pt-BR": {
        "name": "Português",
        "html_lang": "pt-BR",
        "app": "Remover Fundo",
        "full_name": "Remover Fundo: Recortar Foto",
        "nav_home": "Visão geral",
        "nav_help": "Ajuda",
        "nav_privacy": "Privacidade",
        "papers": [("Branco estúdio", "#f8f7f4"), ("Cinza papel", "#dcdad4"), ("Areia", "#e4d9c8"), ("Sálvia", "#d4ddd3"), ("Névoa", "#d3dce6"), ("Grafite", "#2a2c30")],
        "contact_title": "Contato e suporte",
        "contact_body": f"Dúvidas ou problemas no Remover Fundo: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>.",
        "updated": f"Atualizado em {UPDATED} · {BUNDLE_ID} · Hayri Odabaş",
        "hub": {
            "lede": "Recorte de produtos no aparelho com papel infinito de estúdio e sombra vinda da própria silhueta.",
            "help_desc": "Guia de Em pé e Estendido, lâmpada, Borda limpa, pincel, lotes e Pro.",
            "privacy_desc": "Processamento local via Apple Vision, sem envio de fotos, sem conta e sem rastreadores.",
        },
        "help": {
            "title": "Ajuda e guia",
            "lede": "Coloque fotos de produtos em um fundo infinito limpo, processado inteiramente no iPhone ou iPad.",
            "steps_title": "Como usar",
            "steps": [
                ("Escolha uma foto ou teste os exemplos", "Toque em Escolher foto ou experimente primeiro a caneca e o suéter na tela inicial."),
                ("Em pé, Estendido e Lâmpada", "Em Luz escolha Em pé ou Estendido e arraste na foto para mudar o lado da sombra grátis."),
                ("Borda limpa e pincel", "Borda limpa remove halos coloridos do fundo antigo; em Refinar use o pincel com lupa e desfazer."),
                ("Estilos, exportação e lotes", "Grátis até 1600 px sem marca-d'água. Pro (compra única) libera resolução total, 5 papéis extras, cores lisas com sombra, 4:5/3:4/16:9, seleção de vários objetos e lotes de até 30 fotos."),
            ],
            "faq_title": "Perguntas frequentes",
            "faq": [
                ("Minhas fotos vão para a nuvem?", "Não. Todo o recorte roda localmente no dispositivo com Apple Vision."),
                ("Como apagar edições salvas?", "Abra Ajustes › Apagar todas as edições salvas."),
                ("Restaurar compra Pro", "Use Restaurar compra nos Ajustes com a mesma Conta Apple (reembolsos em reportaproblem.apple.com)."),
            ],
        },
        "privacy": {
            "title": "Política de Privacidade",
            "lede": "O Remover Fundo processa todas as fotos no próprio aparelho e não coleta dados pessoais.",
            "summary_title": "Resumo",
            "rows": [
                ("Processamento", "100% local com Apple Vision. Nenhum arquivo sai do aparelho."),
                ("Fotos", "Importação pelo seletor do sistema; permissão apenas de adicionar ao salvar."),
                ("Armazenamento", "Projetos e preferências salvos apenas localmente."),
                ("Análise e anúncios", "Nenhum SDK de terceiros, nenhuma telemetria, nenhuma conta."),
                ("Compra", f"Compra única ({IAP_ID}) processada pela Apple StoreKit."),
            ],
            "sections": [
                ("Sem coleta de dados", "Não coletamos, vendemos ou compartilhamos imagens, identificadores ou métricas."),
                ("Exclusão", "Apague suas edições nos Ajustes do app ou desinstale o aplicativo."),
                ("Contato", f"Dúvidas sobre privacidade: {CONTACT_EMAIL}."),
            ],
        },
    },
    "ru": {
        "name": "Русский",
        "html_lang": "ru",
        "app": "Удалить фон",
        "full_name": "Удалить фон: Вырезать объект",
        "nav_home": "Обзор",
        "nav_help": "Справка",
        "nav_privacy": "Конфиденциальность",
        "papers": [("Студийный белый", "#f8f7f4"), ("Серая бумага", "#dcdad4"), ("Песочный", "#e4d9c8"), ("Шалфей", "#d4ddd3"), ("Туман", "#d3dce6"), ("Графит", "#2a2c30")],
        "contact_title": "Контакты и поддержка",
        "contact_body": f"Вопросы и отзывы о приложении «Удалить фон»: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>.",
        "updated": f"Обновлено {UPDATED} · {BUNDLE_ID} · Hayri Odabaş",
        "hub": {
            "lede": "Отделение товара от фона на устройстве и бумажная циклорама с тенью по форме объекта.",
            "help_desc": "Руководство по режимам «Стоит/Лежит», свету, «Чистому краю», кисти, пакетам и Pro.",
            "privacy_desc": "Локальная обработка Apple Vision, без загрузки снимков, аккаунтов и трекеров.",
        },
        "help": {
            "title": "Справка и руководство",
            "lede": "Готовьте снимки товаров на бесшовной бумажной циклораме прямо на iPhone или iPad.",
            "steps_title": "Как работать",
            "steps": [
                ("Выберите фото или пример", "Откройте снимок из медиатеки или попробуйте кружку и свитер на главном экране."),
                ("Стоит / Лежит и лампа", "В разделе «Свет» выберите постановку и проведите по фото, чтобы бесплатно сменить сторону тени."),
                ("Чистый край и кисть", "«Чистый край» убирает цветной ореол старого фона; в «Правке» доступна кисть с лупой и отменой мазков."),
                ("Стили, экспорт и пакеты", "Бесплатный экспорт — до 1600 px без водяного знака. Pro (разовая покупка) открывает полное разрешение, 5 тонов бумаги, однотонные фоны с тенью, 4:5/3:4/16:9, выбор объектов и пакеты до 30 фото."),
            ],
            "faq_title": "Частые вопросы",
            "faq": [
                ("Фотографии загружаются на сервер?", "Нет. Вся сегментация выполняется локально через Apple Vision."),
                ("Как удалить сохранённые правки?", "Откройте Настройки › Удалить все сохранённые правки."),
                ("Восстановление Pro", "Нажмите «Восстановить покупку» в Настройках с тем же Аккаунтом Apple (возврат через reportaproblem.apple.com)."),
            ],
        },
        "privacy": {
            "title": "Политика конфиденциальности",
            "lede": "«Удалить фон» обрабатывает снимки на устройстве и не собирает личные данные.",
            "summary_title": "Коротко",
            "rows": [
                ("Обработка", "Полностью на устройстве через Apple Vision. Без выгрузки."),
                ("Фото", "Системный выбор фото при импорте; только добавление при сохранении."),
                ("Хранение", "Проекты и настройки хранятся только локально на устройстве."),
                ("Аналитика и реклама", "Отсутствуют. Сторонние SDK не используются."),
                ("Покупка", f"Разовая покупка ({IAP_ID}) через Apple StoreKit."),
            ],
            "sections": [
                ("Данные не собираются", "Мы не собираем, не храним и не передаём снимки, идентификаторы или статистику."),
                ("Удаление данных", "Удалите правки в Настройках приложения или удалите само приложение."),
                ("Контакты", f"По вопросам конфиденциальности пишите на {CONTACT_EMAIL}."),
            ],
        },
    },
    "tr": {
        "name": "Türkçe",
        "html_lang": "tr",
        "app": "Arka Plan Silme",
        "full_name": "Arka Plan Silme: Foto Dekupe",
        "nav_home": "Genel Bakış",
        "nav_help": "Yardım",
        "nav_privacy": "Gizlilik Politikası",
        "papers": [("Stüdyo Beyazı", "#f8f7f4"), ("Kâğıt Grisi", "#dcdad4"), ("Kum", "#e4d9c8"), ("Adaçayı", "#d4ddd3"), ("Sis", "#d3dce6"), ("Antrasit", "#2a2c30")],
        "contact_title": "İletişim ve Destek",
        "contact_body": f"Arka Plan Silme için soru, geri bildirim veya gizlilik talepleri: <a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>.",
        "updated": f"Güncelleme {UPDATED} · {BUNDLE_ID} · Hayri Odabaş",
        "hub": {
            "lede": "Ürün fotoğrafını cihazda arka plandan ayırıp kendi siluetinden çıkan gölgeyle stüdyo fonuna oturtun.",
            "help_desc": "Ayakta/Düz serili düzeni, lamba yönü, Temiz Kenar, fırça, toplu işlem ve Pro rehberi.",
            "privacy_desc": "Apple Vision ile cihaz içinde işleme; yükleme, hesap veya izleme SDK’sı yoktur.",
        },
        "help": {
            "title": "Yardım ve Kullanım Rehberi",
            "lede": "Ürün fotoğraflarınızı iPhone veya iPad dışına çıkarmadan dikişsiz stüdyo kâğıdına yerleştirin.",
            "steps_title": "Kullanım adımları",
            "steps": [
                ("Fotoğraf seçin veya örnekle başlayın", "Fotoğraf Seç ile galeriden görsel açın ya da ana ekrandaki kupa ve kazak örnekleriyle tüm araçları deneyin."),
                ("Ayakta / Düz serili ve Lamba", "Işık sekmesinde Ayakta (zemin çizgisine oturan) veya Düz serili düzeni seçin. Görsel üzerinde sürükleyerek veya lamba kaydırıcısıyla gölgenin yönünü ücretsiz değiştirin."),
                ("Temiz Kenar ve elle fırça", "Temiz Kenar eski arka planın kenar piksellerine sızan rengini temizler. İnce Ayar’da kapatıp ham kesimi görebilir, Sil/Geri Getir fırçası ve büyüteçle düzeltebilirsiniz."),
                ("Görünümler, Dışa Aktarma ve Toplu İşlem", "Stüdyo, İlan, Şeffaf PNG ve Katalog (Pro) tek dokunuşla uygulanır. Ücretsiz dışa aktarma 1600 px’e kadar filigransızdır. Pro (tek seferlik) tam boyut, 5 ek kâğıt tonu, düz renk + gölge, 4:5/3:4/16:9 oranlar, çoklu nesne seçimi ve 30 fotoğrafa kadar toplu işlem ekler."),
            ],
            "faq_title": "Sık sorulan sorular",
            "faq": [
                ("Fotoğraflarım bir sunucuya yükleniyor mu?", "Hayır. Nesne ayrıştırma Apple’ın Vision çerçevesiyle tamamen cihazda çalışır."),
                ("Kaydedilmiş düzenlemeleri nasıl silerim?", "Uygulamada Ayarlar › Kaydedilen Tüm Düzenlemeleri Sil adımıyla yerel projeleri temizleyebilirsiniz."),
                ("Fotoğraflar izni ne zaman istenir?", "Fotoğraf seçimi tam galeri erişimi istemeden sistem seçicisiyle çalışır; yalnızca Kaydet dediğinizde Fotoğraflar’a ekleme izni sorulur."),
                ("Pro satın almayı geri yükleme", "Aynı Apple Hesabı ile Ayarlar › Satın Almayı Geri Yükle’ye dokunun. İadeler Apple tarafından reportaproblem.apple.com üzerinden yürütülür."),
            ],
        },
        "privacy": {
            "title": "Gizlilik Politikası",
            "lede": "Arka Plan Silme tüm görselleri cihazda işler, kişisel veri toplamaz ve fotoğraflarınızı karşıya yüklemez.",
            "summary_title": "Özet",
            "rows": [
                ("Görsel işleme", "Apple Vision ile yalnızca cihazda çalışır. Sunucuya aktarım yapılmaz."),
                ("Fotoğraflar erişimi", "Seçim sistem seçicisiyle, kayıt yalnız siz Kaydet dediğinizde ekleme izniyle yapılır."),
                ("Yerel saklama", "Son düzenlemeler ve tercihler yalnızca uygulama klasöründe cihazda tutulur."),
                ("Analiz ve reklam", "Üçüncü taraf analiz, reklam veya izleme SDK’sı yoktur; hesap açılmaz."),
                ("Satın alma", f"Tek seferlik Pro kilidi ({IAP_ID}) yalnızca Apple StoreKit üzerinden işlenir."),
            ],
            "sections": [
                ("Veri Toplanmaz", "Hayri Odabaş; Arka Plan Silme üzerinden hiçbir fotoğraf, kişisel bilgi, kullanım istatistiği veya cihaz kimliği toplamaz ve paylaşmaz."),
                ("Kontrol ve Silme", "Ayarlar’dan tüm kayıtlı düzenlemeleri silebilir veya uygulamayı kaldırarak tüm yerel dosyaları temizleyebilirsiniz."),
                ("İletişim", f"Gizlilik soruları için: {CONTACT_EMAIL}."),
            ],
        },
    },
    "zh-Hans": {
        "name": "简体中文",
        "html_lang": "zh-Hans",
        "app": "抠图",
        "full_name": "抠图: 去除照片背景",
        "nav_home": "概览",
        "nav_help": "帮助",
        "nav_privacy": "隐私政策",
        "papers": [("影棚白", "#f8f7f4"), ("纸灰", "#dcdad4"), ("沙色", "#e4d9c8"), ("鼠尾草绿", "#d4ddd3"), ("雾蓝", "#d3dce6"), ("炭灰", "#2a2c30")],
        "contact_title": "联系与支持",
        "contact_body": f"有关“抠图”的疑问或反馈：<a href=\"mailto:{CONTACT_EMAIL}\">{CONTACT_EMAIL}</a>。",
        "updated": f"更新于 {UPDATED} · {BUNDLE_ID} · Hayri Odabaş",
        "hub": {
            "lede": "全部在本机完成商品抠图，放到无缝影棚背景纸上并生成来自主体轮廓的自然阴影。",
            "help_desc": "立放与平铺、灯光方向、干净边缘、画笔修饰、批量处理与 Pro 说明。",
            "privacy_desc": "由 Apple Vision 在本机处理，不上传照片，无账号，无任何追踪 SDK。",
        },
        "help": {
            "title": "使用帮助",
            "lede": "直接在 iPhone 或 iPad 上把商品放上无缝影棚背景纸，照片不会离开您的设备。",
            "steps_title": "使用步骤",
            "steps": [
                ("选择照片或先试用示例", "轻点“选择照片”，或先使用主屏幕的马克杯和毛衣示例体验全部功能。"),
                ("立放、平铺与灯光", "在“灯光”中选择立放或平铺，并在画面上拖动滑块或手指即可免费改变阴影方向。"),
                ("干净边缘与画笔", "自动去除原背景溢色；在“修饰”中可用带放大镜的画笔擦除或恢复细节，并随时撤销。"),
                ("预设、导出与批量", "免费版支持长边 1600 px 无水印导出；Pro（买断）解锁原图尺寸、5 种纸色、纯色+阴影、4:5/3:4/16:9 画幅、多主体选择及最多 30 张批量处理。"),
            ],
            "faq_title": "常见问题",
            "faq": [
                ("照片会上传到云端吗？", "不会。主体分割完全通过 Apple Vision 在本机运行。"),
                ("如何清除已保存的编辑？", "在应用内打开“设置 › 删除所有已保存的编辑”即可清除本地项目。"),
                ("如何恢复 Pro 购买？", "使用同一 Apple 账户在“设置 › 恢复购买”恢复；退款由 Apple 在 reportaproblem.apple.com 处理。"),
            ],
        },
        "privacy": {
            "title": "隐私政策",
            "lede": "“抠图”在您的设备上处理所有照片，不收集任何个人数据，也不会上传照片。",
            "summary_title": "隐私摘要",
            "rows": [
                ("图像处理", "完全通过 Apple Vision 在本机运行，不连接外部图像服务器。"),
                ("照片访问", "导入使用系统照片选择器；仅在保存结果时请求添加至相册权限。"),
                ("本地存储", "编辑记录与偏好设置仅保存在本机应用目录中。"),
                ("统计与广告", "无第三方分析 SDK、无广告、无账号体系。"),
                ("内购", f"一次性买断解锁（{IAP_ID}）仅通过 Apple StoreKit 完成。"),
            ],
            "sections": [
                ("不收集数据", "开发者不会收集、存储、出售或分享任何照片、设备标识或使用数据。"),
                ("删除控制", "您可以随时在应用设置中清空已保存的编辑，或卸载应用删除全部本地文件。"),
                ("联系我们", f"隐私相关事宜请联系 {CONTACT_EMAIL}。"),
            ],
        },
    },
}


def render_swatches(papers: list[tuple[str, str]]) -> str:
    items = [
        f'<span class="swatch"><i style="background:{hex_c}"></i>{html.escape(name)}</span>'
        for name, hex_c in papers
    ]
    return '<div class="swatches">' + "".join(items) + "</div>"


def render_lang_bar(current_code: str, page: str, root_rel: str) -> str:
    pills = []
    for code, loc in LOCALES.items():
        href = f"{root_rel}{code}/{page}"
        cls = "lang-pill active" if code == current_code else "lang-pill"
        pills.append(f'<a class="{cls}" href="{href}" hreflang="{html.escape(loc["html_lang"])}">{html.escape(loc["name"])}</a>')
    return '<div class="lang-bar">' + "".join(pills) + "</div>"


def shell(title: str, app_name: str, kicker: str, lede: str, body: str, loc: dict, code: str, page: str, root_rel: str) -> str:
    icon_src = f"{root_rel}app-icon.png"
    home_href = f"{root_rel}{code}/index.html" if root_rel else f"{code}/index.html"
    help_href = f"{root_rel}{code}/help.html" if root_rel else f"{code}/help.html"
    priv_href = f"{root_rel}{code}/privacy.html" if root_rel else f"{code}/privacy.html"
    lang_bar = render_lang_bar(code, page, root_rel)
    return f"""<!doctype html>
<html lang="{html.escape(loc['html_lang'])}">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>{html.escape(title)} — {html.escape(app_name)}</title>
<meta name="description" content="{html.escape(lede)}">
<style>
{CSS}
</style>
</head>
<body>
<div class="sweep-rule" aria-hidden="true"></div>
<main>
<header class="masthead">
  <img src="{icon_src}" alt="{html.escape(app_name)}">
  <div>
    <div class="kicker">{html.escape(kicker)}</div>
    <h1>{html.escape(title)}</h1>
  </div>
</header>
<p class="lede">{html.escape(lede)}</p>
<nav class="top-nav">
  <a href="{home_href}">{html.escape(loc['nav_home'])}</a>
  <a href="{help_href}">{html.escape(loc['nav_help'])}</a>
  <a href="{priv_href}">{html.escape(loc['nav_privacy'])}</a>
  <a href="{BASE_URL}/help.html">{html.escape(LOCALES['en-US']['app'])} EN</a>
</nav>
{lang_bar}
{body}
<section class="panel">
  <strong>{html.escape(loc['contact_title'])}</strong>
  {loc['contact_body']}
</section>
<footer>{html.escape(loc['updated'])}</footer>
</main>
</body>
</html>
"""


def build_help_body(loc: dict) -> str:
    h = loc["help"]
    parts = [render_swatches(loc["papers"]), f"<h2>{html.escape(h['steps_title'])}</h2>"]
    for title, desc in h["steps"]:
        parts.append(f'<div class="panel"><strong>{html.escape(title)}</strong>{html.escape(desc)}</div>')
    parts.append(f"<h2>{html.escape(h['faq_title'])}</h2>")
    for q, a in h["faq"]:
        parts.append(f'<div class="panel"><strong>{html.escape(q)}</strong>{html.escape(a)}</div>')
    return "\n".join(parts)


def build_privacy_body(loc: dict) -> str:
    p = loc["privacy"]
    rows = "\n".join(
        f"<tr><th>{html.escape(k)}</th><td>{html.escape(v)}</td></tr>"
        for k, v in p["rows"]
    )
    parts = [
        f"<h2>{html.escape(p['summary_title'])}</h2>",
        f"<table>{rows}</table>",
    ]
    for title, desc in p["sections"]:
        parts.append(f'<div class="panel"><strong>{html.escape(title)}</strong>{html.escape(desc)}</div>')
    return "\n".join(parts)


def build_hub_body(loc: dict, code: str, root_rel: str) -> str:
    h = loc["hub"]
    help_href = f"{root_rel}{code}/help.html"
    priv_href = f"{root_rel}{code}/privacy.html"
    return f"""{render_swatches(loc['papers'])}
<div class="cards">
  <a class="card" href="{help_href}">
    <strong>{html.escape(loc['nav_help'])}</strong>
    <span>{html.escape(h['help_desc'])}</span>
  </a>
  <a class="card" href="{priv_href}">
    <strong>{html.escape(loc['nav_privacy'])}</strong>
    <span>{html.escape(h['privacy_desc'])}</span>
  </a>
</div>"""


def main() -> None:
    (ROOT / ".nojekyll").write_text("", encoding="utf-8")
    for code, loc in LOCALES.items():
        d = ROOT / code
        d.mkdir(parents=True, exist_ok=True)
        (d / "index.html").write_text(
            shell(loc["full_name"], loc["app"], loc["app"], loc["hub"]["lede"], build_hub_body(loc, code, "../"), loc, code, "index.html", "../"),
            encoding="utf-8",
        )
        (d / "help.html").write_text(
            shell(loc["help"]["title"], loc["app"], loc["full_name"], loc["help"]["lede"], build_help_body(loc), loc, code, "help.html", "../"),
            encoding="utf-8",
        )
        (d / "privacy.html").write_text(
            shell(loc["privacy"]["title"], loc["app"], loc["full_name"], loc["privacy"]["lede"], build_privacy_body(loc), loc, code, "privacy.html", "../"),
            encoding="utf-8",
        )

    en = LOCALES["en-US"]
    (ROOT / "index.html").write_text(
        shell(en["full_name"], en["app"], en["app"], en["hub"]["lede"], build_hub_body(en, "en-US", ""), en, "en-US", "index.html", ""),
        encoding="utf-8",
    )
    (ROOT / "help.html").write_text(
        shell(en["help"]["title"], en["app"], en["full_name"], en["help"]["lede"], build_help_body(en), en, "en-US", "help.html", ""),
        encoding="utf-8",
    )
    (ROOT / "privacy.html").write_text(
        shell(en["privacy"]["title"], en["app"], en["full_name"], en["privacy"]["lede"], build_privacy_body(en), en, "en-US", "privacy.html", ""),
        encoding="utf-8",
    )
    print(f"Generated {len(LOCALES)} locales + root pages in {ROOT}")


if __name__ == "__main__":
    main()
