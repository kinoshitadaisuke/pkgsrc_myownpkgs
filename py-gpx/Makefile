# $NetBSD$

DISTNAME=	gpx-2025.1.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	geography python
MASTER_SITES=	${MASTER_SITE_PYPI:=g/gpx/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/gpx/
COMMENT=	pure Python package for reading and manipulating GPX files
LICENSE=	gnu-gpl-v3

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none

BUILD_DEPENDS+=	${PYPKGPREFIX}-uv-build>=0.9.11:../../devel/py-uv-build

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
