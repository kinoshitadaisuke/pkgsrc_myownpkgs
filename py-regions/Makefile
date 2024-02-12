# $NetBSD$

DISTNAME=	regions-0.8
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=r/regions/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/regions/
COMMENT=	Python package for region handling for astronomical images
LICENSE=	modified-bsd

USE_LANGUAGES+=	c c++
PYTHON_VERSIONS_INCOMPATIBLE=	27 37

DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=0:../../devel/py-setuptools_scm
DEPENDS+=	${PYPKGPREFIX}-wheel>=0:../../devel/py-wheel
DEPENDS+=	${PYPKGPREFIX}-cython>=0.29.30:../../devel/py-cython
DEPENDS+=	${PYPKGPREFIX}-extension-helpers>=0:../../devel/py-extension-helpers
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.18:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-astropy>=5.0:../../pkgsrc_myownpkgs/py-astropy
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=3.1:../../graphics/py-matplotlib

# url2pkg-marker (please do not remove this line.)
.include "../../lang/python/wheel.mk"
.include "../../math/py-numpy/buildlink3.mk"
.include "../../mk/bsd.pkg.mk"
