# $NetBSD$

DISTNAME=	pre_commit_hooks-5.0.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/pre_commit_hooks/pre-commit-hooks/}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=p/pre_commit_hooks/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/pre_commit_hooks/
COMMENT=	Some out-of-the-box hooks for pre-commit
LICENSE=	mit

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-ruamel-yaml>=0.15:../../devel/py-ruamel-yaml
DEPENDS+=	${PYPKGPREFIX}-tomli>=1.1.0:../../textproc/py-tomli
DEPENDS+=	${PYPKGPREFIX}-covdefaults>=0:../../pkgsrc_myownpkgs/py-covdefaults
DEPENDS+=	${PYPKGPREFIX}-coverage>=6.0.2:../../devel/py-coverage
DEPENDS+=	${PYPKGPREFIX}-test>=0:../../devel/py-test

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
