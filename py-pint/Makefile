# $NetBSD$

DISTNAME=	Pint-0.22
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:tl}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=P/Pint/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/Pint/
COMMENT=	Defining, operating, and manipulating physical quantities
LICENSE=	modified-bsd

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27 37 38

DEPENDS+=	${PYPKGPREFIX}-typing-extensions>=0:../../devel/py-typing-extensions
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.19.5:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-uncertainties>=3.1.6:../../math/py-uncertainties
DEPENDS+=	${PYPKGPREFIX}-babel>=2.8:../../devel/py-babel
DEPENDS+=	${PYPKGPREFIX}-pandas>=0.3:../../math/py-pandas
DEPENDS+=	${PYPKGPREFIX}-xarray>=0:../../math/py-xarray
DEPENDS+=	${PYPKGPREFIX}-dask>=0:../../wip/py-dask
DEPENDS+=	${PYPKGPREFIX}-mip>=0:../../pkgsrc_myownpkgs/py-mip
DEPENDS+=	${PYPKGPREFIX}-setuptools>=61:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=3.4.3:../../devel/py-setuptools_scm
DEPENDS+=	${PYPKGPREFIX}-wheel>=0:../../devel/py-wheel

TEST_DEPENDS+=	${PYPKGPREFIX}-test>=0:../../devel/py-test
TEST_DEPENDS+=	${PYPKGPREFIX}-test-mpl>=0:../../wip/py-test-mpl
TEST_DEPENDS+=	${PYPKGPREFIX}-test-cov>=0:../../devel/py-test-cov
TEST_DEPENDS+=	${PYPKGPREFIX}-test-subtests>=0:../../devel/py-test-subtests

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
