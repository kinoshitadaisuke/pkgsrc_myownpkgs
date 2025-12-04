# $NetBSD$

DISTNAME=	xyzservices-2025.11.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	geography python
MASTER_SITES=	${MASTER_SITE_PYPI:=x/xyzservices/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/geopandas/xyzservices
COMMENT=	Source of XYZ tiles providers
LICENSE=	modified-bsd

TOOL_DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=0:../../devel/py-setuptools_scm

USE_LANGUAGES=	# none

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
