# $NetBSD$

DISTNAME=	sphinx_markdown_builder-0.6.10
PKGNAME=	${PYPKGPREFIX}-${DISTNAME:S/_markdown_/-markdown-/}
CATEGORIES=	textproc python
MASTER_SITES=	${MASTER_SITE_PYPI:=s/sphinx_markdown_builder/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/sphinx_markdown_builder/
COMMENT=	Sphinx extension to add markdown generation support
LICENSE=	mit

# TODO: Extract dependencies from pyproject.toml

USE_LANGUAGES=	# none

DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-docutils>=0:../../textproc/py-docutils
DEPENDS+=	${PYPKGPREFIX}-sphinx>=0:../../textproc/py-sphinx
DEPENDS+=	${PYPKGPREFIX}-tabulate>=0:../../textproc/py-tabulate

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
