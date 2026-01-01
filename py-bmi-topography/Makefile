# $NetBSD$

DISTNAME=	bmi_topography-0.9.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/_/-/}
CATEGORIES=	geography python
MASTER_SITES=	${MASTER_SITE_PYPI:=b/bmi_topography/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/bmi_topography/
COMMENT=	Fetch and cache land elevation data from OpenTopography
LICENSE=	mit

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-requests>=0:../../devel/py-requests
DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-click>=0:../../devel/py-click
DEPENDS+=	${PYPKGPREFIX}-yaml>=0:../../textproc/py-yaml
DEPENDS+=	${PYPKGPREFIX}-xarray>=0:../../math/py-xarray
DEPENDS+=	${PYPKGPREFIX}-rioxarray>=0:../../pkgsrc_myownpkgs/py-rioxarray
DEPENDS+=	${PYPKGPREFIX}-bmipy>=0:../../pkgsrc_myownpkgs/py-bmipy

.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
