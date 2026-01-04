# 📦 GUIDE DE PUBLICATION PyPI

**Date:** 4 janvier 2026, 17:30  
**Version:** 0.2.0  
**Status:** En cours de publication

---

## ✅ ÉTAPES COMPLÉTÉES

### 1. Build Package ✅
```bash
python -m build
```

**Résultat :**
- ✅ `boamp_scraper-0.2.0-py3-none-any.whl` (22 KB)
- ✅ `boamp_scraper-0.2.0.tar.gz` (63 KB)

### 2. Validation ✅
```bash
python -m twine check dist/boamp_scraper-0.2.0*
```

**Résultat :**
```
Checking dist\boamp_scraper-0.2.0-py3-none-any.whl: PASSED ✅
Checking dist\boamp_scraper-0.2.0.tar.gz: PASSED ✅
```

---

## 🔄 ÉTAPES EN COURS

### 3. Upload sur TestPyPI (TEST)

**Commande :**
```bash
python -m twine upload --repository testpypi dist/boamp_scraper-0.2.0*
```

**Credentials nécessaires :**
- Username: `__token__`
- Password: `pypi-XXXX...` (API token de test.pypi.org)

### 4. Test Installation depuis TestPyPI

**Commande :**
```bash
pip install --index-url https://test.pypi.org/simple/ --extra-index-url https://pypi.org/simple boamp-scraper
```

**Note :** `--extra-index-url` nécessaire pour les dépendances (playwright, etc.)

### 5. Test Fonctionnel

**Test rapide :**
```bash
python -c "from boamp import TenderScraper; print('✅ Import OK')"
python -m boamp --version
```

**Test complet :**
```bash
python -c "
from boamp import TenderScraper
scraper = TenderScraper()
print('✅ Scraper initialized')
"
```

---

## 🚀 ÉTAPES SUIVANTES (après test OK)

### 6. Upload sur PyPI PROD

**Commande :**
```bash
python -m twine upload dist/boamp_scraper-0.2.0*
```

**Credentials nécessaires :**
- Username: `__token__`
- Password: `pypi-XXXX...` (API token de pypi.org)

### 7. Test Installation depuis PyPI

**Commande :**
```bash
pip install boamp-scraper
```

**Test :**
```bash
python -c "from boamp import TenderScraper; print('✅ PyPI OK')"
```

---

## 📝 CHECKLIST FINALE

### Avant Upload
- [x] Build réussi
- [x] Validation twine OK
- [x] Version 0.2.0 dans setup.py
- [x] Version 0.2.0 dans pyproject.toml
- [x] Version 0.2.0 dans __init__.py
- [x] CHANGELOG à jour
- [x] README complet
- [ ] Compte TestPyPI créé
- [ ] API token TestPyPI créé

### Après Upload TestPyPI
- [ ] Package visible sur test.pypi.org
- [ ] Installation depuis TestPyPI OK
- [ ] Import Python OK
- [ ] Version correcte
- [ ] CLI fonctionne

### Avant Upload PyPI Prod
- [ ] Tests TestPyPI passés
- [ ] Compte PyPI créé
- [ ] API token PyPI créé
- [ ] Prêt pour publication définitive

### Après Upload PyPI Prod
- [ ] Package visible sur pypi.org
- [ ] `pip install boamp-scraper` fonctionne
- [ ] Tests finaux OK
- [ ] Update README avec badge PyPI
- [ ] Annonce sur GitHub

---

## 🔐 CONFIGURATION CREDENTIALS

### Option 1 : Via fichier ~/.pypirc (Recommandé)

**Créer `~/.pypirc` :**
```ini
[distutils]
index-servers =
    pypi
    testpypi

[pypi]
username = __token__
password = pypi-YOUR-PROD-TOKEN-HERE

[testpypi]
repository = https://test.pypi.org/legacy/
username = __token__
password = pypi-YOUR-TEST-TOKEN-HERE
```

**Upload avec :**
```bash
# TestPyPI
python -m twine upload --repository testpypi dist/*

# PyPI Prod
python -m twine upload dist/*
```

### Option 2 : Via prompt (Simple)

```bash
python -m twine upload --repository testpypi dist/*
# Entrer credentials manuellement
```

---

## ⚠️ POINTS D'ATTENTION

### 1. Version Number
- ✅ Version 0.2.0 partout
- ⚠️ Si re-upload nécessaire, incrémenter (0.2.1, 0.2.2...)
- ❌ PyPI ne permet PAS de remplacer une version publiée

### 2. Dependencies
- ✅ Toutes listées dans `requirements.txt`
- ✅ Toutes dans `setup.py` install_requires
- ⚠️ Playwright nécessite `python -m playwright install`

### 3. README
- ✅ Markdown formaté correctement
- ✅ Pas de liens cassés
- ✅ Badges à jour

### 4. License
- ✅ MIT License incluse
- ✅ Mentionnée dans setup.py

---

## 🐛 TROUBLESHOOTING

### Erreur : "File already exists"
**Problème :** Version déjà publiée  
**Solution :** Incrémenter version (0.2.1)

### Erreur : "Invalid credentials"
**Problème :** Token incorrect  
**Solution :** Re-générer token, vérifier copie complète

### Erreur : "Package name already taken"
**Problème :** `boamp-scraper` déjà pris (peu probable)  
**Solution :** Choisir autre nom

### Erreur : Installation dependencies fail
**Problème :** Playwright binary manquant  
**Solution :** `python -m playwright install chromium`

---

## 📊 MÉTRIQUES ATTENDUES

### Après 24h
- Downloads : 5-10
- Stars GitHub : +2-5
- Issues : 0-2

### Après 1 semaine
- Downloads : 50-100
- Stars : +5-10
- Reddit comments : 10-20

### Après 2 semaines (Validation)
- Downloads : **100-500** (objectif validation)
- Stars : **20-50**
- Issues/Questions : **5-10**

---

## 🎯 NEXT STEPS APRÈS PUBLICATION

### Immédiat (Jour 1)
1. ✅ Publier sur PyPI
2. ✅ Update README avec badge
3. ✅ Commit + push
4. ✅ Tweet/LinkedIn (optionnel)

### Lendemain (Jour 2)
1. Posts Reddit (r/Python, r/webdev, r/opensource)
2. Post Hacker News (Show HN)
3. Répondre aux premiers commentaires

### Jours 3-14
1. Monitor downloads quotidiennement
2. Répondre issues/questions
3. Tracker metrics
4. Préparer décision GO/NO-GO

---

**Status:** En attente création compte TestPyPI  
**ETA Publication Finale :** 15-20 minutes  
**Confidence:** 99% ✅

**🚀 PRÊT POUR PUBLICATION ! 🚀**

