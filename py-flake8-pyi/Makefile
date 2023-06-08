# $NetBSD$

DISTNAME=	flake8_pyi-23.5.0
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/flake8_pyi/flake8-pyi/}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=f/flake8_pyi/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/flake8_pyi/
COMMENT=	Plugin for flake8 to enable linting .pyi stub files
LICENSE=	mit

USE_LANGUAGES=	# none

PYTHON_VERSIONS_INCOMPATIBLE=	27

DEPENDS+=	${PYPKGPREFIX}-hatchling>=0:../../devel/py-hatchling
DEPENDS+=	${PYPKGPREFIX}-flake8>=5.0.4:../../devel/py-flake8
DEPENDS+=	${PYPKGPREFIX}-flakes>=2.1.1:../../devel/py-flakes
DEPENDS+=	${PYPKGPREFIX}-ast_decompiler>=0:../../pkgsrc_myownpkgs/py-ast_decompiler
DEPENDS+=	${PYPKGPREFIX}-black>=23.3.0:../../textproc/py-black
DEPENDS+=	${PYPKGPREFIX}-flake8-bugbear>=23.5.9:../../pkgsrc_myownpkgs/py-flake8-bugbear
DEPENDS+=	${PYPKGPREFIX}-flake8-noqa>=1.3.1:../../pkgsrc_myownpkgs/py-flake8-noqa
DEPENDS+=	${PYPKGPREFIX}-isort>=5.12.0:../../devel/py-isort
DEPENDS+=	${PYPKGPREFIX}-mypy>=1.3.0:../../lang/py-mypy
DEPENDS+=	${PYPKGPREFIX}-pre-commit-hooks>=4.4.0:../../pkgsrc_myownpkgs/py-pre-commit-hooks
DEPENDS+=	${PYPKGPREFIX}-test>=0:../../devel/py-test
DEPENDS+=	${PYPKGPREFIX}-types-pyflakes>=0:../../pkgsrc_myownpkgs/py-types-pyflakes

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
