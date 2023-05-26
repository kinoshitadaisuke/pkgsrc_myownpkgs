# $NetBSD$

DISTNAME=	asdf-astropy-0.4.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	math python
MASTER_SITES=	${MASTER_SITE_PYPI:=a/asdf-astropy/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/asdf-astropy/
COMMENT=	Extension library for ASDF to provide support for Astropy
LICENSE=	modified-bsd

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27 37 38

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=60:../../devel/py-setuptools
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=3.4:../../devel/py-setuptools_scm
BUILD_DEPENDS+=	${PYPKGPREFIX}-wheel>=0:../../devel/py-wheel

DEPENDS+=	${PYPKGPREFIX}-asdf>=2.13:../../pkgsrc_myownpkgs/py-asdf
DEPENDS+=	${PYPKGPREFIX}-asdf_coordinates_schemas>=0.1.0:../../wip/py-asdf_coordinates_schemas
DEPENDS+=	${PYPKGPREFIX}-asdf_transform_schemas>=0.2.2:../../wip/py-asdf_transform_schemas
DEPENDS+=	${PYPKGPREFIX}-astropy>=5.0.4:../../pkgsrc_myownpkgs/py-astropy
DEPENDS+=	${PYPKGPREFIX}-numpy>=1.20.0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-packaging>=19:../../devel/py-packaging

DEPENDS+=	${PYPKGPREFIX}-docutils>=0:../../textproc/py-docutils
DEPENDS+=	graphviz>=0:../../graphics/graphviz
DEPENDS+=	${PYPKGPREFIX}-matplotlib>=0:../../graphics/py-matplotlib
DEPENDS+=	${PYPKGPREFIX}-sphinx>=0:../../textproc/py-sphinx
DEPENDS+=	${PYPKGPREFIX}-sphinx-astropy>=0:../../textproc/py-sphinx-astropy
DEPENDS+=	${PYPKGPREFIX}-sphinx-automodapi>=0:../../textproc/py-sphinx-automodapi
DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy

TEST_DEPENDS+=	${PYPKGPREFIX}-coverage>=0:../../devel/py-coverage
TEST_DEPENDS+=	${PYPKGPREFIX}-test-astropy>=0:../../pkgsrc_myownpkgs/py-test-astropy
TEST_DEPENDS+=	${PYPKGPREFIX}-scipy>=0:../../math/py-scipy

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
