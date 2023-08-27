# $NetBSD$

GITHUB_PROJECT=	jupytext
DISTNAME=	1.15.1
GITHUB_TAG=	refs/tags/v${DISTNAME}
PKGNAME=	${PYPKGPREFIX}-${GITHUB_PROJECT}-${DISTNAME}
CATEGORIES=	textproc python
MASTER_SITES=	${MASTER_SITE_GITHUB:=mwouts/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/mwouts/jupytext
COMMENT=	Jupyter notebooks as Markdown documents, Julia, Python or R
LICENSE=	mit

WRKSRC=	${WRKDIR}/${GITHUB_PROJECT}-${DISTNAME}

BUILD_DEPENDS+=	${PYPKGPREFIX}-jupyter_packaging>=0.7.9:../../devel/py-jupyter_packaging
BUILD_DEPENDS+=	${PYPKGPREFIX}-jupyterlab>=3:../../pkgsrc_myownpkgs/py-jupyterlab
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=40.8.0:../../devel/py-setuptools
BUILD_DEPENDS+=	${PYPKGPREFIX}-wheel>=0:../../devel/py-wheel

BUILD_DEPENDS+=	${PYPKGPREFIX}-flake8>=0:../../devel/py-flake8
BUILD_DEPENDS+=	${PYPKGPREFIX}-isort>=0:../../devel/py-isort
BUILD_DEPENDS+=	${PYPKGPREFIX}-black>=0:../../textproc/py-black
BUILD_DEPENDS+=	${PYPKGPREFIX}-test>=3.6:../../devel/py-test
BUILD_DEPENDS+=	${PYPKGPREFIX}-test-randomly>=0:../../devel/py-test-randomly
BUILD_DEPENDS+=	${PYPKGPREFIX}-test-cov>=0:../../devel/py-test-cov
BUILD_DEPENDS+=	${PYPKGPREFIX}-notebook>=0:../../www/py-notebook
BUILD_DEPENDS+=	${PYPKGPREFIX}-jupyter_client>=0:../../devel/py-jupyter_client
BUILD_DEPENDS+=	${PYPKGPREFIX}-nbconvert>=0:../../www/py-nbconvert
BUILD_DEPENDS+=	${PYPKGPREFIX}-ipykernel>=0:../../devel/py-ipykernel
BUILD_DEPENDS+=	${PYPKGPREFIX}-sphinx-gallery>=0:../../textproc/py-sphinx-gallery
BUILD_DEPENDS+=	${PYPKGPREFIX}-pre-commit>=0:../../wip/py-pre-commit
BUILD_DEPENDS+	${PYPKGPREFIX}-gitpython>=0:../../devel/py-gitpython

DEPENDS+=	${PYPKGPREFIX}-nbformat>=5.1.2:../../www/py-nbformat
DEPENDS+=	${PYPKGPREFIX}-yaml>=0:../../textproc/py-yaml
DEPENDS+=	${PYPKGPREFIX}-toml>=0:../../textproc/py-toml
DEPENDS+=	${PYPKGPREFIX}-markdown-it-py>=1.0.0:../../textproc/py-markdown-it-py
DEPENDS+=	${PYPKGPREFIX}-mdit-py-plugins>=0:../../pkgsrc_myownpkgs/py-mdit-py-plugins

USE_LANGUAGES=	c++

post-install:
	cd ${DESTDIR}${PREFIX}/bin && \
	${MV} jupytext jupytext-${PYVERSSUFFIX} || ${TRUE}
	cd ${DESTDIR}${PREFIX}/bin && \
	${MV} jupytext-config jupytext-config-${PYVERSSUFFIX} || ${TRUE}

#.include "../../lang/python/egg.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
