# $NetBSD$

DISTNAME=	jupyterlite-0.1.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=j/jupyterlite/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/jupyterlite/
COMMENT=	JupyterLab distribution that runs entirely in the browser
LICENSE=	modified-bsd

USE_LANGUAGES=	# none

DEPENDS+=	nodejs>=0:../../lang/nodejs
DEPENDS+=	yarn>=0:../../devel/yarn
DEPENDS+=	${PYPKGPREFIX}-doit>=0.34:../../pkgsrc_myownpkgs/py-doit
DEPENDS+=	${PYPKGPREFIX}-hatch>=1.6.3:../../pkgsrc_myownpkgs/py-hatch
DEPENDS+=	${PYPKGPREFIX}-twine>=0:../../net/py-twine
DEPENDS+=	${PYPKGPREFIX}-requests-cache>=0:../../wip/py-requests-cache
DEPENDS+=	${PYPKGPREFIX}-pkginfo>=0:../../devel/py-pkginfo
DEPENDS+=	${PYPKGPREFIX}-jupyter_core>=4.7:../../devel/py-jupyter_core
DEPENDS+=	${PYPKGPREFIX}-jupyterlab>=3.5.3:../../pkgsrc_myownpkgs/py-jupyterlab
DEPENDS+=	${PYPKGPREFIX}-importlib-metadata>=0:../../devel/py-importlib-metadata

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
