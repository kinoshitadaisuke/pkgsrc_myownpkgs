# $NetBSD$

DISTNAME=	pytype-2023.7.12
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/pytype/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/pytype/
COMMENT=	Python type inferencer
LICENSE=	apache-2.0

USE_LANGUAGES+=	c
USE_LANGUAGES+=	c++

DEPENDS+=	${PYPKGPREFIX}-setuptools>=40.8.0:../../devel/py-setuptools
DEPENDS+=	ninja-build>=0:../../devel/ninja-build
DEPENDS+=	${PYPKGPREFIX}-wheel>=0:../../devel/py-wheel
DEPENDS+=	${PYPKGPREFIX}-pybind11>=2.10.1:../../devel/py-pybind11

# url2pkg-marker (please do not remove this line.)
.include "../../devel/py-pybind11/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
