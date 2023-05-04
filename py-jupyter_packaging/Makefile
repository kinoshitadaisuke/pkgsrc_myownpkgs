# $NetBSD$

DISTNAME=	jupyter_packaging-0.12.3
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	pkgsrc_myownpkgs
MASTER_SITES=	${MASTER_SITE_PYPI:=j/jupyter_packaging/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/jupyter_packaging/
COMMENT=	Tools to help build and install Jupyter Python packages
LICENSE=	modified-bsd

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-hatchling>=1.5.0:../../devel/py-hatchling
DEPENDS+=	${PYPKGPREFIX}-packaging>0:../../devel/py-packaging
DEPENDS+=	${PYPKGPREFIX}-tomlkit>0:../../textproc/py-tomlkit
DEPENDS+=	${PYPKGPREFIX}-setuptools>=60.2.0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-wheel>0:../../devel/py-wheel
DEPENDS+=	${PYPKGPREFIX}-deprecation>0:../../devel/py-deprecation

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
