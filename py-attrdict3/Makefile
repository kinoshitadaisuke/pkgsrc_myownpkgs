# $NetBSD$

DISTNAME=	attrdict3-2.0.2
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=a/attrdict3/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/pirofti/AttrDict3
COMMENT=	A dict with attribute-style access
LICENSE=	mit

DEPENDS+=	${PYPKGPREFIX}-six>=0:../../lang/py-six
TEST_DEPENDS+=	${PYPKGPREFIX}-nose>=1.0:../../devel/py-nose
TEST_DEPENDS+=	${PYPKGPREFIX}-coverage>=0:../../devel/py-coverage

USE_LANGUAGES=	# none

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
