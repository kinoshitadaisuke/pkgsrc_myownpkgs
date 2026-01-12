# $NetBSD$

DISTNAME=	types-urllib3-1.26.25.14
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	devel python
MASTER_SITES=	${MASTER_SITE_PYPI:=t/types-urllib3/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://github.com/python/typeshed
COMMENT=	Typing stubs for urllib3
LICENSE=	apache-2.0

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-typing-extensions>=0:../../devel/py-typing-extensions
DEPENDS+=	${PYPKGPREFIX}-aiohttp>=3.8.4:../../www/py-aiohttp
DEPENDS+=	${PYPKGPREFIX}-black>=23.3.0:../../textproc/py-black
DEPENDS+=	${PYPKGPREFIX}-flake8>=6.0.0:../../devel/py-flake8
DEPENDS+=	${PYPKGPREFIX}-flake8_bugbear>=23.5.9:../../pkgsrc_myownpkgs/py-flake8-bugbear
DEPENDS+=	${PYPKGPREFIX}-flake8-noqa>=1.3.1:../../pkgsrc_myownpkgs/py-flake8-noqa
DEPENDS+=	${PYPKGPREFIX}-flake8-pyi>=23.5.0:../../pkgsrc_myownpkgs/py-flake8-pyi
DEPENDS+=	${PYPKGPREFIX}-isort>=5.12.0:../../devel/py-isort
DEPENDS+=	${PYPKGPREFIX}-mypy>=1.3.0:../../lang/py-mypy
DEPENDS+=	${PYPKGPREFIX}-packaging>=23.1:../../devel/py-packaging
DEPENDS+=	${PYPKGPREFIX}-pathspec>=0.11.1:../../devel/py-pathspec
DEPENDS+=	${PYPKGPREFIX}-pre-commit-hooks>=4.4.0:../../pkgsrc_myownpkgs/py-pre-commit-hooks
DEPENDS+=	${PYPKGPREFIX}-pycln>=2.1.5:../../pkgsrc_myownpkgs/py-pycln
DEPENDS+=	${PYPKGPREFIX}-pytype>=2023.6.2:../../pkgsrc_myownpkgs/py-pytype
DEPENDS+=	${PYPKGPREFIX}-yaml>=6.0:../../textproc/py-yaml
DEPENDS+=	${PYPKGPREFIX}-stubdefaulter>=0.1.0:../../pkgsrc_myownpkgs/py-stubdefaulter
DEPENDS+=	${PYPKGPREFIX}-termcolor>=2.3:../../devel/py-termcolor
DEPENDS+=	${PYPKGPREFIX}-tomli>=2.0.1:../../textproc/py-tomli
DEPENDS+=	${PYPKGPREFIX}-tomlkit>=0.11.8:../../textproc/py-tomlkit
DEPENDS+=	${PYPKGPREFIX}-types-yaml>=6.0.12.7:../../textproc/py-types-yaml
DEPENDS+=	${PYPKGPREFIX}-types-setuptools>=67.5.0.0:../../devel/py-types-setuptools
DEPENDS+=	${PYPKGPREFIX}-typing-extensions>=0:../../devel/py-typing-extensions

.include "../../lang/python/egg.mk"
.include "../../mk/bsd.pkg.mk"
