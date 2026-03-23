# $NetBSD$

DISTNAME=	pynndescent-0.6.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/pynndescent/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/pynndescent/
COMMENT=	Nearest neighbor descent for approximate nearest neighbors
LICENSE=	modified-bsd

USE_LANGUAGES=	# none

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=61.2:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-scikit-learn>=0.18:../../math/py-scikit-learn
DEPENDS+=	${PYPKGPREFIX}-scipy>=1.0:../../math/py-scipy
DEPENDS+=	${PYPKGPREFIX}-numba>=0.55.0:../../math/py-numba
DEPENDS+=	${PYPKGPREFIX}-llvmlite>=0.38:../../devel/py-llvmlite
DEPENDS+=	${PYPKGPREFIX}-joblib>=0.11:../../devel/py-joblib

.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
