# $NetBSD$

DISTNAME=	sgp4-2.24
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=s/sgp4/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/sgp4/
COMMENT=	Python implementation of the SGP4 satellite tracking algorithm
LICENSE=	mit

USE_LANGUAGES+=	c c++

DEPENDS+=	${PYPKGPREFIX}-numpy>=1.14:../../math/py-numpy

# url2pkg-marker (please do not remove this line.)
.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
