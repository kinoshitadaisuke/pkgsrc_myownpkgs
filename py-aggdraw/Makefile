# $NetBSD$

DISTNAME=	aggdraw-1.3.16
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	graphics python
MASTER_SITES=	${MASTER_SITE_PYPI:=a/aggdraw/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/pytroll/aggdraw
COMMENT=	High quality drawing interface for PIL
LICENSE=	Python (MIT style)

USE_LANGUAGES=	c c++

DEPENDS+=	${PYPKGPREFIX}-packaging>=0:../../devel/py-packaging
DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools

TEST_DEPENDS+=	${PYPKGPREFIX}-test>=0:../../devel/py-test
TEST_DEPENDS+=	${PYPKGPREFIX}-Pillow>=0:../../graphics/py-Pillow

.include "../../graphics/freetype2/buildlink3.mk"
.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
