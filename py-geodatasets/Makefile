# $NetBSD$

DISTNAME=	geodatasets-2025.12.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	python geography
MASTER_SITES=	${MASTER_SITE_PYPI:=g/geodatasets/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/geodatasets/
COMMENT=	Fetch links or download and cache spatial data example files
LICENSE=	modified-bsd

USE_LANGUAGES=	# none

DEPENDS+=       ${PYPKGPREFIX}-pooch>=0:../../devel/py-pooch

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
