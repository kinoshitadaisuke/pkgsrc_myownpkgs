# $NetBSD$

DISTNAME=	pytest-astropy-0.10.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/pytest-astropy/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/pytest-astropy/
COMMENT=	meta-package pulls in the dependencies that are used by astropy
LICENSE=	modified-bsd

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=30.3.0:../../devel/py-setuptools
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=0:../../devel/py-setuptools_scm
BUILD_DEPENDS+=	${PYPKGPREFIX}-wheel>=0:../../devel/py-wheel

DEPENDS+=	${PYPKGPREFIX}-test>=4.6:../../devel/py-test
DEPENDS+=	${PYPKGPREFIX}-test-doctestplus>=0.11.0:../../devel/py-test-doctestplus
DEPENDS+=	${PYPKGPREFIX}-test-remotedata>=0.3.1:../../wip/py-test-remotedata
DEPENDS+=	${PYPKGPREFIX}-test-astropy-header>=0.1.2:../../pkgsrc_myownpkgs/py-test-astropy-header
DEPENDS+=	${PYPKGPREFIX}-test-arraydiff>=0.1:../../pkgsrc_myownpkgs/py-test-arraydiff
DEPENDS+=	${PYPKGPREFIX}-test-filter-subpackage>=0.1:../../pkgsrc_myownpkgs/py-test-filter-subpackage
DEPENDS+=	${PYPKGPREFIX}-test-cov>=2.3.1:../../devel/py-test-cov
DEPENDS+=	${PYPKGPREFIX}-test-mock>=2.0:../../devel/py-test-mock
DEPENDS+=	${PYPKGPREFIX}-attrs>=19.2.0:../../devel/py-attrs
DEPENDS+=	${PYPKGPREFIX}-hypothesis>=5.1:../../devel/py-hypothesis

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
