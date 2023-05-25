# $NetBSD$

DISTNAME=	pytest-arraydiff-0.5.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/pytest-arraydiff/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/pytest-arraydiff/
COMMENT=	pytest plugin for generation and comparison of data arrays
LICENSE=	modified-bsd

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=30.3.0:../../devel/py-setuptools
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=0:../../devel/py-setuptools_scm
BUILD_DEPENDS+=	${PYPKGPREFIX}-wheel>=0:../../devel/py-wheel

DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy
DEPENDS+=	${PYPKGPREFIX}-test>=4.6:../../devel/py-test

TEST_DEPENDS+=	${PYPKGPREFIX}-astropy>=0:../../pkgsrc_myownpkgs/py-astropy
TEST_DEPENDS+=	${PYPKGPREFIX}-pandas>=0:../../math/py-pandas
TEST_DEPENDS+=	${PYPKGPREFIX}-tables>=0:../../math/py-tables

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
