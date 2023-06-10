# $NetBSD$

GITHUB_TAG=	refs/tags/v${PKGVERSION_NOREV}
DISTNAME=	MyST-NB-0.17.2
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/MyST-NB/myst-nb/}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_GITHUB:=executablebooks/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/executablebooks/MyST-NB/
COMMENT=	Parse and execute ipynb files in Sphinx
LICENSE=	modified-bsd

WRKSRC=	${WRKDIR}/${DISTNAME}

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27 37

DEPENDS+=	${PYPKGPREFIX}-flit_core>=3.4:../../devel/py-flit_core
DEPENDS+=	${PYPKGPREFIX}-importlib-metadata>=0:../../devel/py-importlib-metadata
DEPENDS+=	${PYPKGPREFIX}-ipython>=0:../../devel/py-ipython
DEPENDS+=	${PYPKGPREFIX}-jupyter-cache>=0:../../pkgsrc_myownpkgs/py-jupyter-cache
DEPENDS+=	${PYPKGPREFIX}-nbclient>=0.2:../../www/py-nbclient
DEPENDS+=	${PYPKGPREFIX}-myst-parser>=0.18.0:../../pkgsrc_myownpkgs/py-myst-parser
DEPENDS+=	${PYPKGPREFIX}-nbformat>=5.0:../../www/py-nbformat
DEPENDS+=	${PYPKGPREFIX}-yaml>=0:../../textproc/py-yaml
DEPENDS+=	${PYPKGPREFIX}-sphinx>=4:../../textproc/py-sphinx
DEPENDS+=	${PYPKGPREFIX}-typing-extensions>=0:../../devel/py-typing-extensions
DEPENDS+=	${PYPKGPREFIX}-ipykernel>0:../../devel/py-ipykernel
DEPENDS+=	${PYPKGPREFIX}-pre-commit>=0:../../wip/py-pre-commit

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
