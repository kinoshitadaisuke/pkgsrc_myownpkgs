# $NetBSD$

DISTNAME=	notebook_shim-0.2.3
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=n/notebook_shim/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/notebook_shim/
COMMENT=	For switching to Jupyter Server
LICENSE=	modified-bsd

DEPENDS+=	${PYPKGPREFIX}-jupyter_server>=1.8:../../pkgsrc_myownpkgs/py-jupyter_server

PYTHON_VERSIONS_INCOMPATIBLE=	27

USE_LANGUAGES=	# none

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
