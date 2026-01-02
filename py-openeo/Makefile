# $NetBSD$

DISTNAME=	openeo-python-client-0.47.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	geography python
MASTER_SITES=	${MASTER_SITE_GITHUB:=Open-EO/}
GITHUB_TAG=	refs/tags/v${PKGVERSION_NOREV}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/Open-EO/openeo-python-client
COMMENT=	Client API for openEO
LICENSE=	apache-2.0

WRKSRC=	${WRKDIR}/${DISTNAME}

TOOL_DEPENDS+=	${PYPKGPREFIX}-arrow>=0:../../time/py-arrow
TOOL_DEPENDS+=	${PYPKGPREFIX}-boto3>=0:../../net/py-boto3
TOOL_DEPENDS+=	${PYPKGPREFIX}-botocore>=0:../../net/py-botocore
TOOL_DEPENDS+=	${PYPKGPREFIX}-dirty-equals>=0.8.0:../../devel/py-dirty-equals
TOOL_DEPENDS+=	${PYPKGPREFIX}-flake8>=5.0.0:../../devel/py-flake8
TOOL_DEPENDS+=	${PYPKGPREFIX}-httpretty>=1.1.4:../../www/py-httpretty
TOOL_DEPENDS+=	${PYPKGPREFIX}-mock>=0:../../devel/py-mock
TOOL_DEPENDS+=	${PYPKGPREFIX}-moto>=5.0.0:../../net/py-moto
TOOL_DEPENDS+=	${PYPKGPREFIX}-netCDF4>=1.7.0:../../math/py-netCDF4
TOOL_DEPENDS+=	${PYPKGPREFIX}-proj>=3.2.0:../../geography/py-proj
TOOL_DEPENDS+=	${PYPKGPREFIX}-requests-mock>=1.8.0:../../devel/py-requests-mock
TOOL_DEPENDS+=	${PYPKGPREFIX}-sphinx>=0:../../textproc/py-sphinx
TOOL_DEPENDS+=	${PYPKGPREFIX}-sphinx-autodoc-typehints>=2.2.3:../../textproc/py-sphinx-autodoc-typehints
TOOL_DEPENDS+=	${PYPKGPREFIX}-test>=4.5.0:../../devel/py-test
TOOL_DEPENDS+=	${PYPKGPREFIX}-time-machine>=2.13.0:../../time/py-time-machine
TOOL_DEPENDS+=	${PYPKGPREFIX}-geopandas>=0.14:../../pkgsrc_myownpkgs/py-geopandas
TOOL_DEPENDS+=	${PYPKGPREFIX}-myst-parser>=0:../../pkgsrc_myownpkgs/py-myst-parser
TOOL_DEPENDS+=	${PYPKGPREFIX}-pystac>=0.7.5:../../pkgsrc_myownpkgs/py-pystac
TOOL_DEPENDS+=	${PYPKGPREFIX}-dateutil>=2.7.0:../../time/py-dateutil
#TOOL_DEPENDS+=	# TODO: sphinx-autodoc-annotation>=0
#TOOL_DEPENDS+=	# TODO: types-boto3-s3>=0
#TOOL_DEPENDS+=	# TODO: types-boto3-sts>=0
TOOL_DEPENDS+=	${PYPKGPREFIX}-urllib3>=0:../../www/py-urllib3
DEPENDS+=	${PYPKGPREFIX}-deprecated>=1.2.12:../../devel/py-deprecated
#DEPENDS+=	${PYPKGPREFIX}-oschmod>=0.3.12;sys_platform=="win32":../../pkgsrc_myownpkgs/py-oschmod
DEPENDS+=	${PYPKGPREFIX}-pandas>0.20.0:../../math/py-pandas
DEPENDS+=	${PYPKGPREFIX}-requests>=2.26.0:../../devel/py-requests
DEPENDS+=	${PYPKGPREFIX}-urllib3>=1.9.0:../../www/py-urllib3
DEPENDS+=	${PYPKGPREFIX}-xarray>=0.12.3:../../math/py-xarray
#DEPENDS+=	# TODO: importlib_resources;python_version<'3.9'>=0
DEPENDS+=	# TODO: pystac>=1.5.0
DEPENDS+=	${PYPKGPREFIX}-shapely>=1.6.4:../../pkgsrc_myownpkgs/py-shapely
TEST_DEPENDS+=	${PYPKGPREFIX}-arrow>=10.0.1:../../time/py-arrow
TEST_DEPENDS+=	${PYPKGPREFIX}-dirty-equals>=0.8.0:../../devel/py-dirty-equals
TEST_DEPENDS+=	${PYPKGPREFIX}-flake8>=5.0.0:../../devel/py-flake8
TEST_DEPENDS+=	${PYPKGPREFIX}-httpretty>=1.1.4:../../www/py-httpretty
TEST_DEPENDS+=	${PYPKGPREFIX}-mock>=0:../../devel/py-mock
TEST_DEPENDS+=	${PYPKGPREFIX}-moto>=5.0.0:../../net/py-moto
TEST_DEPENDS+=	${PYPKGPREFIX}-netCDF4>=1.7.0:../../math/py-netCDF4
TEST_DEPENDS+=	${PYPKGPREFIX}-proj>=3.2.0:../../geography/py-proj
TEST_DEPENDS+=	${PYPKGPREFIX}-requests-mock>=1.8.0:../../devel/py-requests-mock
TEST_DEPENDS+=	${PYPKGPREFIX}-test>=4.5.0:../../devel/py-test
TEST_DEPENDS+=	${PYPKGPREFIX}-time-machine>=2.13.0:../../time/py-time-machine
#TEST_DEPENDS+=	# TODO: geopandas>=0.14;python_version>='3.9'
#TEST_DEPENDS+=	# TODO: geopandas>=0
#TEST_DEPENDS+=	# TODO: pystac-client>=0.7.5
#TEST_DEPENDS+=	# TODO: python-dateutil>=2.7.0
#TEST_DEPENDS+=	# TODO: urllib3<2.3.0>=0

USE_LANGUAGES=	# none

BUILDLINK_API_DEPENDS.py-numpy+=	${PYPKGPREFIX}-numpy>=1.17.0
.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
