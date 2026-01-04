# Notes sur la structure réelle de BOAMP.fr

**Date:** 4 janvier 2026  
**Source:** Inspection de https://www.boamp.fr/pages/recherche/

## Structure HTML

BOAMP utilise Angular.js avec rendu dynamique. Les données sont chargées via JavaScript.

### Container principal
```html
<ul class="no-list-style ng-scope" id="toplist" 
    ng-init="..." 
    ods-results="items" 
    ods-results-context="boamp" 
    ods-results-max="10">
```

### Élément de résultat (tender)
```html
<li class="fr-pb-0 ng-binding ng-scope" ng-repeat="(i,item) in items">
    <div class="card-notification fr-callout fr-callout--boamp fr-py-2v fr-px-2w fr-px-md-3w fr-mb-4w ng-scope">
        ...
    </div>
</li>
```

### Données extraites

#### 1. Titre (Objet du marché)
- **Selector:** `.card-notification h2 span[ng-bind-html="item.fields.objet"]`
- **Field Angular:** `item.fields.objet`
- **Exemple:** "Prestation de service de collecte, de traitement et valorisation des déchets - (7 lots)"

#### 2. Organisme (Acheteur)
- **Selector:** `span[ng-bind-html="item.fields.nomacheteur"]`
- **Field Angular:** `item.fields.nomacheteur`
- **Exemple:** "CONSEIL DEPARTEMENTAL DU VAR"

#### 3. Numéro d'avis (ID)
- **Selector:** `label[ng-bind]` ou `input[id^="checkboxes-select-avis-"]`
- **Field Angular:** `item.fields.idweb`
- **Exemple:** "26-12"

#### 4. Date de publication
- **Selector:** `span[ng-bind]` contenant "Publié le"
- **Field Angular:** `item.fields.dateparution`
- **Format:** "4 janvier 2026"

#### 5. URL de détail
- **Format:** `/pages/avis?q=idweb:"<idweb>"`
- **Base:** `https://www.boamp.fr`
- **Exemple:** `https://www.boamp.fr/pages/avis?q=idweb:"26-12"`

#### 6. Date limite de réponse
- **Selector:** Texte contenant "Date limite de réponse"
- **Field Angular:** `avis_gestion.INDEXATION.DATE_LIMITE_REPONSE`
- **Format:** "05/02/2026 à 16h00"

#### 7. Département
- **Selector:** `span[ng-repeat="dept in tab_dept"]`
- **Field Angular:** `item.fields.code_departement`
- **Exemple:** "83"

#### 8. Type d'avis
- **Selector:** `span[ng-bind="item.fields.nature_libelle"]`
- **Field Angular:** `item.fields.nature_libelle`
- **Exemple:** "Avis de marché"

#### 9. Procédure
- **Selector:** `span[ng-bind="item.fields.procedure_libelle"]`
- **Field Angular:** `item.fields.procedure_libelle`
- **Exemple:** "Procédure Ouverte"

## Selectors CSS finaux (après rendu Angular)

```python
# Container de résultats
RESULTS_CONTAINER = "#toplist"

# Chaque carte de tender
TENDER_CARDS = ".card-notification.fr-callout.fr-callout--boamp"

# À l'intérieur d'une carte :
TITLE_SELECTOR = "h2 span[ng-bind-html*='objet']"
ORGANISME_SELECTOR = "span[ng-bind-html*='nomacheteur']"
ID_SELECTOR = "label[for^='checkboxes-select-avis-']"
DATE_SELECTOR = "span[ng-bind*='dateparution']"
LINK_SELECTOR = "h2 a[href*='/pages/avis']"
```

## Attente du rendu

**Important:** Il faut attendre que Angular charge et rende les données.

```python
# 1. Goto page
await page.goto(url)

# 2. Attendre l'élément #toplist
await page.wait_for_selector("#toplist", timeout=30000)

# 3. Attendre que les cartes apparaissent
await page.wait_for_selector(".card-notification", timeout=10000)

# 4. Attendre un peu pour le rendu complet
await asyncio.sleep(2)

# 5. Extraire les données
cards = await page.query_selector_all(".card-notification")
```

## Budget / Prix

**⚠️ Problème:** Le budget n'est pas toujours visible dans la liste des résultats.  
Il faut aller sur la page de détail pour l'obtenir.

**Options:**
1. Retourner `budget=0` dans la liste
2. Faire une requête supplémentaire pour chaque tender (lent)
3. Extraire depuis l'API BOAMP si disponible

## Pagination

Pour les résultats suivants, BOAMP utilise :
- `ods-results-max="10"` : 10 résultats par page par défaut
- Peut être modifié via l'URL ou les paramètres de recherche

## Catégories

Les catégories ne sont pas directement visibles dans les résultats.  
On peut les déduire des mots-clés dans l'objet ou utiliser l'analyse du contenu.

---

**Next steps:**
1. ✅ Identifier les selectors
2. ⏳ Mettre à jour boamp/scraper.py
3. ⏳ Tester avec vraies données
4. ⏳ Gérer la pagination
5. ⏳ Optimiser les performances

