# $NetBSD$

DISTNAME=	jupyterlab_server-2.25.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=j/jupyterlab_server/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/jupyterlab_server/
COMMENT=	JupyterLab Server sits between JupyterLab and Jupyter Server
LICENSE=	modified-bsd

DEPENDS+=	${PYPKGPREFIX}-hatchling>=1.5:../../devel/py-hatchling
DEPENDS+=	${PYPKGPREFIX}-babel>=2.10:../../devel/py-babel
DEPENDS+=	${PYPKGPREFIX}-importlib-metadata>=4.8.3:../../devel/py-importlib-metadata
DEPENDS+=	${PYPKGPREFIX}-jinja2>=3.0.3:../../textproc/py-jinja2
DEPENDS+=	${PYPKGPREFIX}-json5>=0.9.0:../../pkgsrc_myownpkgs/py-json5
DEPENDS+=	${PYPKGPREFIX}-jsonschema>=4.17.3:../../textproc/py-jsonschema
DEPENDS+=	${PYPKGPREFIX}-jupyter_server>=1.21:../../pkgsrc_myownpkgs/py-jupyter_server
DEPENDS+=	${PYPKGPREFIX}-packaging>=21.3:../../devel/py-packaging
DEPENDS+=	${PYPKGPREFIX}-requests>=2.28:../../devel/py-requests

USE_PKGLOCALEDIR=	yes
USE_LANGUAGES=		# none

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
