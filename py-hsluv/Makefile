# $NetBSD$

DISTNAME=	hsluv-5.0.3
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	graphics python
MASTER_SITES=	${MASTER_SITE_PYPI:=h/hsluv/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://www.hsluv.org
COMMENT=	Human-friendly HSL
LICENSE=	mit

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=38.6.0:../../devel/py-setuptools

USE_LANGUAGES=	# none

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
