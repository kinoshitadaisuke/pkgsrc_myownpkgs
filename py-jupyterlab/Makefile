# $NetBSD$

DISTNAME=	jupyterlab-4.0.0rc1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	www python
MASTER_SITES=	${MASTER_SITE_PYPI:=j/jupyterlab/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/jupyterlab/
COMMENT=	Next-generation user interface for Project Jupyter
LICENSE=	modified-bsd

USE_LANGUAGES=	# none
CHECK_INTERPRETER=	no

DEPENDS+=	${PYPKGPREFIX}-hatchling>=1.5.0:../../devel/py-hatchling
DEPENDS+=	${PYPKGPREFIX}-async-lru>=1.0.0:../../pkgsrc_myownpkgs/py-async-lru
DEPENDS+=	${PYPKGPREFIX}-importlib-metadata>=4.8.3:../../devel/py-importlib-metadata
DEPENDS+=	${PYPKGPREFIX}-importlib-resources>=1.4:../../devel/py-importlib-resources
DEPENDS+=	${PYPKGPREFIX}-ipykernel>0:../../devel/py-ipykernel
DEPENDS+=	${PYPKGPREFIX}-jinja2>=3.0.3:../../textproc/py-jinja2
DEPENDS+=	${PYPKGPREFIX}-jupyter_core>0:../../devel/py-jupyter_core
DEPENDS+=	${PYPKGPREFIX}-jupyter-lsp>=2.0.0:../../pkgsrc_myownpkgs/py-jupyter-lsp
DEPENDS+=	${PYPKGPREFIX}-jupyter_server>=2.4.0:../../pkgsrc_myownpkgs/py-jupyter_server
DEPENDS+=	${PYPKGPREFIX}-jupyterlab_server>=2.19.0:../../pkgsrc_myownpkgs/py-jupyterlab_server
DEPENDS+=	${PYPKGPREFIX}-notebook_shim>=0.2:../../pkgsrc_myownpkgs/py-notebook_shim
DEPENDS+=	${PYPKGPREFIX}-packaging>0:../../devel/py-packaging
DEPENDS+=	${PYPKGPREFIX}-traitlets>0:../../devel/py-traitlets
DEPENDS+=	${PYPKGPREFIX}-tornado>=6.2.0:../../www/py-tornado
DEPENDS+=	${PYPKGPREFIX}-tomli>0:../../textproc/py-tomli
DENEPDS+=	${PYPKGPREFIX}-build>0:../../devel/py-build
DEPENDS+=	${PYPKGPREFIX}-ipython>=8.4.0:../../devel/py-ipython
DEPENDS+=	${PYPKGPREFIX}-nbclassic>0:../../pkgsrc_myownpkgs/py-nbclassic
DEPENDS+=	${PYPKGPREFIX}-notebook>0:../../www/py-notebook
DEPENDS+=	npm>0:../../lang/npm
DEPENDS+=	${PYPKGPREFIX}-json-logger>0:../../pkgsrc_myownpkgs/py-json-logger

PYTHON_VERSIONS_INCOMPATIBLE=	27 37

MESSAGE_SUBST+=	PYVERSSUFFIX=${PYVERSSUFFIX}

post-install:
	cd ${DESTDIR}${PREFIX}/bin && \
	${MV} jlpm jlpm-${PYVERSSUFFIX} || ${TRUE}
.for name in lab labextension labhub
	cd ${DESTDIR}${PREFIX}/bin && \
	${MV} jupyter-${name} jupyter-${name}-${PYVERSSUFFIX} || ${TRUE}
.endfor

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
