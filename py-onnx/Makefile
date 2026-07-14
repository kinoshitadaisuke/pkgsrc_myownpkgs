# $NetBSD$

DISTNAME=	onnx-1.22.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=o/onnx/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/onnx/
COMMENT=	Open Neural Network Exchange
LICENSE=	apache-2.0

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	c++

BUILD_DEPENDS+=	${PYPKGPREFIX}-scikit-build>=0.11:../../devel/py-scikit-build
BUILD_DEPENDS+=	${PYPKGPREFIX}-scikit-build-core>=0.11:../../devel/py-scikit-build-core
DEPENDS+=	protobuf>=0:../../devel/protobuf
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.23.2:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-protobuf>=6.31.1:../../devel/py-protobuf
DEPENDS+=	${PYPKGPREFIX}-typing-extensions>=4.7.1:../../devel/py-typing-extensions
DEPENDS+=	${PYPKGPREFIX}-ml-dtypes>=0.5.4:../../pkgsrc_myownpkgs/py-ml-dtypes

.include "../../devel/protobuf/buildlink3.mk"
.include "../../math/py-numpy/buildlink3.mk"
.include "../../devel/cmake/build.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
