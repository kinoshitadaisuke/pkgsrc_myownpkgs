# $NetBSD$

DISTNAME=	skl2onnx-1.20.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=s/skl2onnx/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/skl2onnx/
COMMENT=	converting scikit-learn models to ONNX
LICENSE=	apache-2.0

# TODO: Extract dependencies from pyproject.toml
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
DEPENDS+=       ${PYPKGPREFIX}-onnx>=1.2.1:../../pkgsrc_myownpkgs/py-onnx
DEPENDS+=       ${PYPKGPREFIX}-scikit-learn>=1.1:../../math/py-scikit-learn

USE_LANGUAGES=	# none

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
