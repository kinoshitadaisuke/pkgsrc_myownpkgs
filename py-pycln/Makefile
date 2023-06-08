# $NetBSD$

DISTNAME=	pycln-2.1.5
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/pycln/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/pycln/
COMMENT=	Formatter for finding and removing unused import statements
LICENSE=	mit

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

DEPENDS+=	${PYPKGPREFIX}-typer>=0.4.1:../../pkgsrc_myownpkgs/py-typer
DEPENDS+=	${PYPKGPREFIX}-yaml>=5.3.1:../../textproc/py-yaml
DEPENDS+=	${PYPKGPREFIX}-pathspec>=0.9.0:../../devel/py-pathspec
DEPENDS+=	${PYPKGPREFIX}-tomlkit>=0.11.1:../../textproc/py-tomlkit
DEPENDS+=	${PYPKGPREFIX}-libcst>=0.3.10:../../lang/py-libcst
DEPENDS+=	${PYPKGPREFIX}-requests>=2.24.0:../../devel/py-requests
DEPENDS+=	${PYPKGPREFIX}-semver>=2.10.2:../../wip/py-semver
DEPENDS+=	${PYPKGPREFIX}-test>=7.0:../../devel/py-test
DEPENDS+=	${PYPKGPREFIX}-test-cov>=4.0.0:../../devel/py-test-cov
DEPENDS+=	${PYPKGPREFIX}-test-randomly>=3.4.1:../../devel/py-test-randomly
DEPENDS+=	${PYPKGPREFIX}-oschmod>=0.3.9:../../pkgsrc_myownpkgs/py-oschmod
DEPENDS+=	${PYPKGPREFIX}-hypothesmith>=0:../../devel/py-hypothesmith

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
