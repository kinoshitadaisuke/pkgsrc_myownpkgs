# $NetBSD$

DISTNAME=	colorful-0.5.6
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=c/colorful/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/colorful/
COMMENT=	Terminal string styling done right, in Python
LICENSE=	mit

DEPENDS+=	${PYPKGPREFIX}-test>=0:../../devel/py-test
DEPENDS+=	${PYPKGPREFIX}-coverage>=0:../../devel/py-coverage
DEPENDS+=	${PYPKGPREFIX}-flake8>=0:../../devel/py-flake8

# url2pkg-marker (please do not remove this line.)
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
