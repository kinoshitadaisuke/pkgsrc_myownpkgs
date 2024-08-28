# $NetBSD$

DISTNAME=	sphinx_changelog-1.4.1
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	textproc python
MASTER_SITES=	${MASTER_SITE_PYPI:=s/sphinx_changelog/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/sphinx_changelog/
COMMENT=	Changelog renderer for sphinx
LICENSE=	modified-bsd

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=0:../../devel/py-setuptools_scm
BUILD_DEPENDS+=	${PYPKGPREFIX}-wheel>=0:../../devel/py-wheel

DEPENDS+=	${PYPKGPREFIX}-sphinx>=0:../../textproc/py-sphinx
DEPENDS+=	${PYPKGPREFIX}-sphinx-automodapi>=0:../../textproc/py-sphinx-automodapi
DEPENDS+=	${PYPKGPREFIX}-towncrier>=22.12.0:../../wip/py-towncrier

TEST_DEPENDS+=	${PYPKGPREFIX}-test>=0:../../devel/py-test
TEST_DEPENDS+=	${PYPKGPREFIX}-test-cov>=0:../../devel/py-test-cov

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
