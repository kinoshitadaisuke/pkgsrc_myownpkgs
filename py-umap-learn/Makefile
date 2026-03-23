# $NetBSD$

DISTNAME=	umap_learn-0.5.11
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=u/umap_learn/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/umap_learn/
COMMENT=	Uniform Manifold Approximation and Projection
LICENSE=	mofified-bsd

USE_LANGUAGES=	# none

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=61:../../devel/py-setuptools
BUILD_DEPENDS+=	${PYPKGPREFIX}-wheel>=0:../../devel/py-wheel
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.23:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-scipy>=1.3.1:../../math/py-scipy
DEPENDS+=	${PYPKGPREFIX}-scikit-learn>=1.6:../../math/py-scikit-learn
DEPENDS+=	${PYPKGPREFIX}-numba>=0.51.2:../../math/py-numba
DEPENDS+=	${PYPKGPREFIX}-tqdm>=0:../../misc/py-tqdm
DEPENDS+=	${PYPKGPREFIX}-pynndescent>=0.5:../../pkgsrc_myownpkgs/py-pynndescent

.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
