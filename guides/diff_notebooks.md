# Como ver o que mudou num jupyter notebook

Instale o [nbdime](https://github.com/jupyter/nbdime) 

	sudo pip install nbdime


Basta usar o comando nbdiff-web

	nbdiff-web ParticleFilter.ipynb ParticleFilter_update.ipynb


O resultado deve ser como a tela abaixo, que mostra de forma visual a diferença 

![Comando nbdiff-web em execução](compare_notebooks_nbdiff_web.png)


Experimente também os comandos:

* nbdiff - mostra a diferença entre dois notebooks no terminal
* nbmerge - ajuda a fazer o merge entre dois notebooks no terminal
* nbmerge-web - ajudar a fazer o merge entre dois notebooks no browser
