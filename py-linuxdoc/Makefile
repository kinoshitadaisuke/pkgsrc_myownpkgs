# $NetBSD$

DISTNAME=	linuxdoc-20260504
PKGNAME=	${PYPKGPREFIX}-${DISTNAME}
CATEGORIES=	textproc python
MASTER_SITES=	${MASTER_SITE_PYPI:=l/linuxdoc/}

MAINTAINER=	pkgsrc-users@NetBSD.org
HOMEPAGE=	https://pypi.org/project/linuxdoc/
COMMENT=	Sphinx-doc extensions and tools to extract documentation
LICENSE=	gnu-gpl-v3

# TODO: Extract dependencies from pyproject.toml

DEPENDS+=	${PYPKGPREFIX}-fspath>=0:../../pkgsrc_myownpkgs/py-fspath
DEPENDS+=	${PYPKGPREFIX}-setuptools>=0:../../devel/py-setuptools
DEPENDS+=	${PYPKGPREFIX}-docutils>=0:../../textproc/py-docutils
DEPENDS+=	${PYPKGPREFIX}-sphinx>=0:../../textproc/py-sphinx

.include "../../lang/python/wheel.mk"
.include "../../mk/bsd.pkg.mk"
