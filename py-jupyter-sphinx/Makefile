# $NetBSD$

GITHUB_TAG=	refs/tags/v${PKGVERSION_NOREV}
DISTNAME=	jupyter-sphinx-0.4.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	textproc python
MASTER_SITES=	${MASTER_SITE_GITHUB:=jupyter/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/jupyter/jupyter-sphinx/
COMMENT=	Jupyter Sphinx Extensions
LICENSE=	modified-bsd

WRKSRC=		${WRKDIR}/${DISTNAME}

DEPENDS+=	${PYPKGPREFIX}-sphinx>=2.4.4:../../textproc/py-sphinx
DEPENDS+=	${PYPKGPREFIX}-ipywidgets>=7.0.0:../../www/py-ipywidgets
DEPENDS+=	${PYPKGPREFIX}-ipython>=0:../../devel/py-ipython
DEPENDS+=	${PYPKGPREFIX}-nbconvert>=5.5:../../www/py-nbconvert
DEPENDS+=	${PYPKGPREFIX}-nbformat>=0:../../www/py-nbformat
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=0:../../graphics/py-matplotlib
DEPENDS+=	${PYPKGPREFIX}-test>=0:../../devel/py-test
DEPENDS+=	bash>=0:../../shells/bash

USE_LANGUAGES=	# none

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
