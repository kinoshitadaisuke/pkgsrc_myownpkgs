# $NetBSD$

DISTNAME=	nanobind-2.12.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=n/nanobind/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/nanobind/
COMMENT=	tiny and efficient C++/Python bindings
LICENSE=	modified-bsd

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	c++

DEPENDS+=	${PYPKGPREFIX}-scikit-build-core>=0.10:../../devel/py-scikit-build-core
DEPENDS+=	eigen3>=0:../../math/eigen3

.include "../../math/eigen3/buildlink3.mk"
.include "../../devel/cmake/build.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
