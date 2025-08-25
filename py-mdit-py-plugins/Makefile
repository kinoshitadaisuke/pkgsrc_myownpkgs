# $NetBSD$

DISTNAME=       mdit_py_plugins-0.5.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/mdit_py_plugins/mdit-py-plugins/}
CATEGORIES=	textproc python
MASTER_SITES=   ${MASTER_SITE_PYPI:=m/mdit_py_plugins/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/executablebooks/mdit-py-plugins/
COMMENT=	Collection of core plugins for markdown-it-py
LICENSE=	mit

USE_LANGUAGES=	# none

WRKSRC=	${WRKDIR}/${DISTNAME}

PYTHON_VERSIONS_INCOMPATIBLE=	27 37

DEPENDS+=	${PYPKGPREFIX}-flit_core>=3.4:../../devel/py-flit_core
DEPENDS+=	${PYPKGPREFIX}-markdown-it-py>=3.0:../../textproc/py-markdown-it-py
DEPENDS+=	${PYPKGPREFIX}-pre-commit>=0:../../wip/py-pre-commit
DEPENDS+=	${PYPKGPREFIX}-coverage>=0:../../devel/py-coverage
DEPENDS+=	${PYPKGPREFIX}-test>=0:../../devel/py-test
DEPENDS+=	${PYPKGPREFIX}-test-cov>=0:../../devel/py-test-cov
DEPENDS+=	${PYPKGPREFIX}-test-regressions>=0:../../pkgsrc_myownpkgs/py-test-regressions

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
