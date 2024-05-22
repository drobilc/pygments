Pygments'
=========

A modified version of the `Pygments <https://pygments.org/>`__ library
with custom lexer and styling for the **STG** (Spineless Tagless
G-machine) language.

Used to render code listings with the
`minted <https://ctan.org/pkg/minted>`__ LaTeX package in
`magistrsko_delo <https://github.com/drobilc/magistrsko-delo>`__.

Installation
------------

To install, make sure git is installed and run the following commands

.. code:: shell

   git clone https://github.com/drobilc/pygments.git
   cd pygments
   pip install .

Development
-----------

To install the package in editable mode, run ``pip install -e .``
command.

Lexer
~~~~~

#. To modify the lexer, edit the
   ```pygments/lexers/stg.py`` </syntax_highlighting/pygments/lexers/stg.py>`__
   file.
#. After making the changes, run ``tox -e mapfiles`` to rebuild the
   lexer mapping.
#. Delete the ``magistrsko_delo/_minted-magistrsko_delo``
   directory to remove cached files and rerun the LaTeX compiler to see
   the changes.

For more information, check out the `Pygments lexer development
documentation <https://pygments.org/docs/lexerdevelopment/>`__.

Styling
~~~~~~~

#. To modify the styling, edit the
   ```pygments/styles/stgyle.py`` </syntax_highlighting/pygments/styles/stgyle.py>`__
   file.
#. After making the changes, run ``tox -e mapfiles`` to rebuild the
   mappings file.
#. Delete the ``magistrsko_delo/_minted-magistrsko_delo``
   directory to remove cached files and rerun the LaTeX compiler to see
   the changes.

For more information, check out the `Pygments style development
documentation <https://pygments.org/docs/styledevelopment/>`__.