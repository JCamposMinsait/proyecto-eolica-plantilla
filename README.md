# proyecto_eolica

El proyecto del día 5: las funciones de limpieza de la telemetría en un módulo de Python, sus tests y una CI/CD en GitHub Actions que pasa los tests en cada cambio y, si lo activas, despliega el proyecto en tu Databricks.

```
proyecto_eolica/
├── src/eolica/limpieza.py        las funciones
├── tests/                         los tests de pytest (conftest.py crea una sesión de Spark local)
├── notebooks/usar_modulo.py       un notebook que usa las funciones sobre tu Bronze
├── databricks.yml                 el bundle: qué se despliega en Databricks
└── .github/workflows/ci_cd.yml    la CI/CD
```

## 1 · Tu repositorio en GitHub

**Con la plantilla (lo normal).** Abre el enlace que te pasa el formador, pulsa **Use this template → Create a new repository**, ponle de nombre `proyecto-eolica`, déjalo privado y créalo.

**A mano, si no hay plantilla.**
1. En GitHub, **New repository**: `proyecto-eolica`, privado y sin README.
2. Descarga el repo del curso (**Code → Download ZIP**), descomprímelo y sube el contenido de la carpeta `proyecto_eolica` con **Add file → Upload files**.
3. Comprueba que se ha subido la carpeta `.github`. Muchos navegadores no suben carpetas que empiezan por punto. Si falta, créala con **Add file → Create new file**, escribiendo como nombre `.github/workflows/ci_cd.yml` y pegando su contenido.

Al crear el repo, la CI arranca sola. Mírala en la pestaña **Actions**: falla, porque falta una función y su test por escribir. Es lo esperado.

## 2 · Conectar Databricks con GitHub

1. En Databricks, arriba a la derecha, tu usuario → **Settings → Linked accounts → Add Git credential**.
2. Elige **GitHub**, pulsa **Link Git account** y autoriza la aplicación de Databricks en GitHub, dándole acceso a `proyecto-eolica`.
3. **Workspace → Create → Git folder**, pega la URL de tu repositorio y pulsa **Create Git folder**.

Ya tienes el repo dentro de Databricks. Lo que cambies ahí se sube a GitHub con un commit, y lo que cambie en GitHub se trae con **Pull**.

## 3 · Trabajar con una rama

1. En el Git folder, pulsa el botón de la rama (arriba, pone `main`) → **Create branch** → `mi-cambio`.
2. Haz los cambios (el lab 5a te dice cuáles).
3. Botón de Git → revisa los cambios → escribe un mensaje → **Commit & Push**.
4. En GitHub, abre una **Pull Request** de `mi-cambio` a `main`. La CI pasa los tests en la propia PR. Cuando esté en verde, haz el **merge**.

## 4 · CD: desplegar en Databricks desde GitHub (opcional)

Con esto, cada merge a `main` despliega el proyecto en tu workspace como un job.

1. En Databricks: **Settings → Developer → Access tokens → Generate new token**. Ponle una duración corta, de 7 días por ejemplo, y copia el token.
2. En GitHub, en tu repo: **Settings → Secrets and variables → Actions**.
   - En **Secrets**, crea `DATABRICKS_HOST`, con la dirección de tu workspace (la del navegador, hasta `.com`), y `DATABRICKS_TOKEN`, con el token.
   - En **Variables**, crea `DESPLEGAR` con el valor `true`. Sin ella, la CD no se ejecuta.
3. Haz un merge a `main`. En **Actions** aparece el paso `desplegar` después de los tests.
4. En Databricks, en **Jobs & Pipelines**, sale el job `[dev tu_usuario] limpieza-eolica`. Ejecútalo.
5. Si tu catálogo no es `formacion`, cambia el valor de `catalogo` en `databricks.yml`.

> En una empresa esto no se hace con el token de una persona, sino con una identidad técnica (un Service Principal), que en la cuenta gratuita no existe. Al acabar el curso, borra el token.

## Pasar los tests en tu ordenador (opcional)

Con Python 3.11 y Java 17: `pip install -r requirements.txt` y `pytest -v`.
