# $NetBSD$

DISTNAME=	huey-2.6.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=h/huey/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/huey/
COMMENT=	little task queue
LICENSE=	mit

USE_LANGUAGES=	# none

# build dependencies
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
# optional dependencies
DEPENDS+=	${PYPKGPREFIX}-redis>=3.0.0:../../databases/py-redis

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
