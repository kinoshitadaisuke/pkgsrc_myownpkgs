# $NetBSD$

DISTNAME=	onnxmltools-1.16.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	pkgsrc_myownpkgs python
MASTER_SITES=	${MASTER_SITE_PYPI:=o/onnxmltools/}

MAINTAINER=	INSERT_YOUR_MAIL_ADDRESS_HERE # or use pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/onnxmltools/
COMMENT=	TODO: Short description of the package
#LICENSE=	# TODO: (see mk/license.mk)

# TODO: Extract dependencies from pyproject.toml
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-onnx>=1.8.1:../../pkgsrc_myownpkgs/py-onnx
DEPENDS+=	${PYPKGPREFIX}-protobuf>=0:../../devel/py-protobuf
DEPENDS+=	${PYPKGPREFIX}-skl2onnx>=1.4.9:../../pkgsrc_myownpkgs/py-skl2onnx

USE_LANGUAGES=	# none

.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
