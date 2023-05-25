# $NetBSD$

DISTNAME=	pytest-astropy-header-0.2.2
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/pytest/test/}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/pytest-astropy-header/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/pytest-astropy-header/
COMMENT=	Pytest plugin to add diagnostic information to the header
LICENSE=	modified-bsd

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=30.3.0:../../devel/py-setuptools
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=0:../../devel/py-setuptools_scm
BUILD_DEPENDS+=	${PYPKGPREFIX}-wheel>=0:../../devel/py-wheel

DEPENDS+=	${PYPKGPREFIX}-test>=4.6:../../devel/py-test

TEST_DEPENDS+=	${PYPKGPREFIX}-numpy>=0:../../math/py-numpy
TEST_DEPENDS+=	${PYPKGPREFIX}-astropy>=4.0:../../pkgsrc_myownpkgs/py-astropy

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
