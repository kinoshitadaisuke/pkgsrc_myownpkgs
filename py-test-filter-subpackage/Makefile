# $NetBSD$

DISTNAME=	pytest-filter-subpackage-0.1.2
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/pytest/test/}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/pytest-filter-subpackage/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/pytest-filter-subpackage/
COMMENT=	Pytest plugin for all code and documentation for a sub-package
LICENSE=	modified-bsd

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=0:../../devel/py-setuptools_scm
BUILD_DEPENDS+=	${PYPKGPREFIX}-wheel>=0:../../devel/py-wheel

DEPENDS+=	${PYPKGPREFIX}-test>=3.0:../../devel/py-test

TEST_DEPENDS+=	${PYPKGPREFIX}-test-doctestplus>=0:../../devel/py-test-doctestplus
TEST_DEPENDS+=	${PYPKGPREFIX}-test-cov>=0:../../devel/py-test-cov

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
