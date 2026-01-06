# $NetBSD$

DISTNAME=	py4j-0.10.9.9
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/py4j/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://www.py4j.org/
COMMENT=	Enables Python programs to dynamically access Java objects
LICENSE=	modified-bsd

USE_LANGUAGES=	# none

TEST_DEPENDS+=	${PYPKGPREFIX}-flake8>=4.0.1:../../devel/py-flake8
TEST_DEPENDS+=	${PYPKGPREFIX}-tox>=2.1.1:../../devel/py-tox
TEST_DEPENDS+=	${PYPKGPREFIX}-test>=7.1.1:../../devel/py-test

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
