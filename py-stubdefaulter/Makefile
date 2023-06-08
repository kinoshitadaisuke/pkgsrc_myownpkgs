# $NetBSD$

DISTNAME=	stubdefaulter-0.1.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=s/stubdefaulter/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/stubdefaulter/
COMMENT=	Autoadd default values to stubs
LICENSE=	mit

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

DEPENDS+=	${PYPKGPREFIX}-hatchling>=1.11.0:../../devel/py-hatchling
DEPENDS+=	${PYPKGPREFIX}-libcst>=0:../../lang/py-libcst
DEPENDS+=	${PYPKGPREFIX}-termcolor>=2:../../devel/py-termcolor
DEPENDS+=	${PYPKGPREFIX}-typeshed_client>=0:../../pkgsrc_myownpkgs/py-typeshed_client
DEPENDS+=	${PYPKGPREFIX}-tomli>=0:../../textproc/py-tomli
DEPENDS+=	${PYPKGPREFIX}-black>=23.3.0:../../textproc/py-black
DEPENDS+=	${PYPKGPREFIX}-flake8-bugbear>=23.6.5:../../pkgsrc_myownpkgs/py-flake8-bugbear
DEPENDS+=       ${PYPKGPREFIX}-flake8-noqa>=1.3.1:../../pkgsrc_myownpkgs/py-flake8-noqa
DEPENDS+=	${PYPKGPREFIX}-isort>=5.12.0:../../devel/py-isort
DEPENDS+=	${PYPKGPREFIX}-mypy>=1.3.0:../../lang/py-mypy
DEPENDS+=	${PYPKGPREFIX}-pre-commit-hooks>=4.4.0:../../pkgsrc_myownpkgs/py-pre-commit-hooks
DEPENDS+=	${PYPKGPREFIX}-test>=0:../../devel/py-test

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
