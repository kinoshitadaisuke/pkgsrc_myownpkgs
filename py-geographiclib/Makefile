# $NetBSD$

DISTNAME=	geographiclib-2.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	geography python
MASTER_SITES=	${MASTER_SITE_PYPI:=g/geographiclib/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/geographiclib/
COMMENT=	Python implementation of the geodesic routines
LICENSE=	mit

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-setuptools>=42:../../devel/py-setuptools

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
