# $NetBSD$

DISTNAME=	pytest_regressions-2.8.2
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/pytest_/test-/}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/pytest-regressions/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/ESSS/pytest-regressions
COMMENT=	Easy to use fixtures to write regression tests
LICENSE=	mit

BUILD_DEPENDS+=	${PYPKGPREFIX}-matplotlib>=0:../../graphics/py-matplotlib
BUILD_DEPENDS+=	${PYPKGPREFIX}-mypy>=0:../../lang/py-mypy
BUILD_DEPENDS+=	${PYPKGPREFIX}-pandas>=0:../../math/py-pandas
BUILD_DEPENDS+=	${PYPKGPREFIX}-Pillow>=0:../../graphics/py-Pillow
BUILD_DEPENDS+=	${PYPKGPREFIX}-pre-commit>=0:../../wip/py-pre-commit
BUILD_DEPENDS+=	${PYPKGPREFIX}-restructuredtext_lint>=0:../../devel/py-restructuredtext_lint
BUILD_DEPENDS+=	${PYPKGPREFIX}-tox>=0:../../devel/py-tox
BUILD_DEPENDS+=	${PYPKGPREFIX}-setuptools_scm>=0:../../devel/py-setuptools_scm
DEPENDS+=	${PYPKGPREFIX}-test-datadir>=1.2.0:../../devel/py-test-datadir
DEPENDS+=	${PYPKGPREFIX}-test>=6.2.0:../../devel/py-test
DEPENDS+=	${PYPKGPREFIX}-yaml>=0:../../textproc/py-yaml

USE_LANGUAGES=	# none

BUILDLINK_DEPENDS.py-numpy+=	build
BUILDLINK_API_DEPENDS.py-numpy+=	${PYPKGPREFIX}-numpy>=0
.include "../../math/py-numpy/buildlink3.mk"
.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
